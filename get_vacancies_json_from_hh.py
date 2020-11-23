import requests
import project_tools.request
from multiprocessing.dummy import Pool as ThreadPool
import pickle
import os
from project_tools.json_tools import *
import time
import bs4


def read_list_from_file(filename):
    with open(filename, 'r') as f:
        x = f.readlines()
        ids = [int(id) for id in x]
    return x

def GeneratorUrlsVaconcies2(start, end):
    base_dir = "F:\\!hh.ru\\bad_ids"
    ids = read_list_from_file(f'{base_dir}\\{str(start).zfill(8)}_{str(end).zfill(8)}_bad.txt')

    ids = [int(id) for id in ids]
    print(len(ids))
    for id in ids:
        print(id)
        yield f"https://api.hh.ru/vacancies/{id}"

def GeneratorUrlsVaconcies(start, end):
    for id in range(start, end):
        yield f"https://api.hh.ru/vacancies/{id}"

def MainFunction(url):
    #cr = project_tools.request.ControlRequestClass()
    tries = 5
    while(tries>0):
        responce = requests.get(url)#cr.GetHTML(url)
        if(responce == '' or responce == 'error'):
            tries -=1
            print(f"one more time... {tries}")
        else:
            vacancy = json.loads(responce)
            #CheckErrorsInVacancy(vacancy)
            return vacancy

def CheckSpesializationOfVacancy(vacancy_json, id_spesialization = '1'):
    if('specializations' in vacancy_json):
        for spesialization in vacancy_json['specializations']:
            try:
                if(spesialization['profarea_id']==id_spesialization):
                    return True
            except Exception:
                print(Exception)
    return False

def CheckErrorsInVacancy(vacansy_json):
    if('errors' in vacansy_json):
        #pp_json(vacansy_json)
        return False
    else:
        return True

def WriteToPickle(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


#скачиваем по блокам вакансии с hh
block_size = 10000
start_id = 00000000
stop_id  = 15000000
threads = 10
main_dir = "f:/!hh.ru/vacancies_pickle_all_add/downloading/"

for i in range(start_id, stop_id, block_size):

    a = str(i).zfill(8)
    b = str(i+block_size).zfill(8)

    filename = f"{main_dir}{a}_{b}.pickle"

    print(filename)
    if(os.path.exists(filename)==False):
        print(filename)
        A = time.time()
        print(f"Генерируем ссылки на очередной блок вакансий: [{i},{i+block_size}]")
        urls = GeneratorUrlsVaconcies2(i,i+block_size)

        pool = ThreadPool(threads)
        vacancies = []
        vacancies = pool.map(MainFunction, urls)

        pool.close()
        pool.join()

        #print(f'Количество вакансий до фильтрации: {len(vacancies)}')

        vacancies = list(filter(None, vacancies))
        #print(f'Количество вакансий после фильтрации None: {len(vacancies)}')

        vacancies = list(filter(CheckErrorsInVacancy, vacancies))
        #print(f'Количество вакансий после фильтрации Пустых_Errors: {len(vacancies)}')

        #vacancies = list(filter(CheckSpesializationOfVacancy, vacancies))
        #print(f'Количество вакансий после фильтрации id_spesialization = 1: {len(vacancies)}')

        #print(vacancies)
        WriteToPickle(filename, vacancies)
        B = time.time()

        a = round((B - A), 2)
        b = ((stop_id - i) / block_size)
        print(a, b, round((a*b)/60/60,2))
        print("=========================================================================")
