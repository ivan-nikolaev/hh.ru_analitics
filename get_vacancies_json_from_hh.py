import os
from tqdm import tqdm
import zipfile
import json
import shutil
import requests
import logging
from multiprocessing.dummy import Pool as ThreadPool
from project_tools.pickle_tools import write_to_pickle

import threading
from concurrent.futures import ThreadPoolExecutor
import time

from tqdm_multi_thread import TqdmMultiThreadFactory



def generator_urls_vacancies(start, end):
    for id in range(start, end):
        yield f"https://api.hh.ru/vacancies/{id}"


def is_error_vacancy(vacansy_json):
    if('errors' in vacansy_json):
        return True
    else:
        return False


def get_vacancy_json(url, tries=10):
    while(tries>0):
        try:
            responce = requests.get(url, timeout=3)
            #print(url, responce, responce.status_code, responce.text)
            if responce.status_code == 200:
                return json.loads(responce.text)
            elif responce.status_code == 404:
                return json.loads(responce.text)

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        except Exception:
            pass
        tries -= 1
        print(f'try one more time {tries}')


    return json.loads('{}')


def multy_thread_downloading_func(urls, threads=10):
    pool = ThreadPool(threads)
    vacancies = pool.map(get_vacancy_json, urls)
    pool.close()
    pool.join()

    return vacancies


#%%

#main_dir = "f:/!hh.ru/vacancies_pickle_all_add/downloading/"
main_dir = "e:/!hh.ru/vacancies_pickle_all_2020"
down_dir = main_dir +'/downloading'

logging.basicConfig(handlers=[logging.FileHandler(filename=f'{main_dir}\\log_downloading_vacancies.log',
                              encoding='utf-8',
                              mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)


#скачиваем по блокам вакансии с hh
block_size, start_id, stop_id = 10000, 30000000, 41000000


if not os.path.exists(main_dir):
    os.mkdir(main_dir)

if not os.path.exists(main_dir):
    shutil.rmtree(down_dir)
    os.mkdir(down_dir)

#%%
for i in tqdm(range(start_id, stop_id, block_size)):

    a, b = str(i).zfill(8), str(i+block_size).zfill(8)

    filename_pkl = f"{down_dir}/{a}_{b}.pkl"
    filename_zip = filename_pkl.replace('.pkl','.zip')
    if(os.path.exists(filename_zip)==True):
        continue

    print(f" block urls: [{i},{i+block_size}]")
    urls = generator_urls_vacancies(i, i + block_size)

    vacancies = multy_thread_downloading_func(urls)

    filter_func = lambda vacancy: False if ('errors' in vacancy) or (vacancy=={}) or (vacancy==None) else True
    vacancies_filtered = list(filter(filter_func, vacancies))

    #print(len(vacancies), len(vacancies_filtered))

    logging.info(f"Save to file: {filename_pkl}")
    logging.info(f"Filtering   : {len(vacancies)}, {len(vacancies_filtered)}")

    write_to_pickle(filename_pkl, vacancies_filtered)

    with zipfile.ZipFile(filename_pkl.replace('.pkl','.zip'), 'w', zipfile.ZIP_DEFLATED) as myzip:
        myzip.write(filename_pkl, os.path.basename(filename_pkl))
    os.remove(filename_pkl)