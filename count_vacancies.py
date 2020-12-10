#%%

from project_tools.os_tools import generator_files_in_dir
from project_tools.vacancies_tools import extract_zip_by_vacancy
from project_tools.vacancies_tools import get_vacancies_from_dir_with_zips
from tqdm import tqdm
from project_tools.pickle_tools import write_to_pickle

import logging

logging.basicConfig(handlers=[logging.FileHandler(filename=r'F:\!hh.ru\log.log',
                              encoding='utf-8',
                              mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)

#%%
src_dir = r"F:\!hh.ru\vacancies_pickle_all_2020_"

#add_dir = r"F:\!hh.ru\vacancies_pickle_all_zip_add"
#%%

#
# def find_file_with_same_name(name, files):
#     for f in files:
#         if(f.find(name)>=0):
#             return f
#
# files_add = generator_files_in_dir(add_dir)
#
# for file in generator_files_in_dir(src_dir):
#     name = file.split('\\')[-1].split('.')[0]
#
#     file_add = find_file_with_same_name(name, files_add)
#
#     ids = [vacancy['id'] for vacancy in tqdm(extract_zip_by_vacancy(file))]
#     ids_add = [vacancy['id'] for vacancy in tqdm(extract_zip_by_vacancy(file_add))]
#
#     print(len(ids), len(ids_add), len(set(ids).intersection(set(ids_add))))
#     #logging.info(len(ids), len(ids_add), len(set(ids).intersection(set(ids_add))))

#%%
vacancies = []
for vacancy in tqdm(get_vacancies_from_dir_with_zips(src_dir)):
    vacancies.append(vacancy)


#%%
vacancies[100]

#%%
ids = []
i = 1
for vacancy in tqdm(get_vacancies_from_dir_with_zips(src_dir)):
    #print(vacancy['id'])
    ids.append((vacancy['id']))
    if len(ids)==1000000:
        write_to_pickle(f'ids\\ids_{i}.pkl', ids)
        ids = []
        i=i+1

#%%
ids_add = []
for vacancy in tqdm(get_vacancies_from_dir_with_zips(add_dir)):
    #print(vacancy)
    ids_add.append((vacancy['id']))

print(len(ids), len(ids_add))

#%%

print(len(ids_add))