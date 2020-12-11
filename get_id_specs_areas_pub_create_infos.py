#%%


from project_tools.vacancies_tools import get_vacancies_from_dir_with_zips
from tqdm import tqdm
from project_tools.pickle_tools import write_to_pickle

from project_tools.vacancies_tools import get_id_specs_areas_pub_create_infos

import logging

# logging.basicConfig(handlers=[logging.FileHandler(filename=r'F:\!hh.ru\log.log',
#                               encoding='utf-8',
#                               mode='a+')],
#                     format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
#                     datefmt="%F %A %T",
#                     level=logging.INFO)

src_dir = r"F:\!hh.ru\vacancies_pickle_all_2020"

dst_dir = r"F:\!hh.ru\vacancies_id_profareas_specializations_published"


ids = []
block = 1000000
n_block = 1
for i, vacancy_json in enumerate(tqdm((get_vacancies_from_dir_with_zips(src_dir)))):
    ids.append(get_id_specs_areas_pub_create_infos(vacancy_json))

    if len(ids)%1000000==0:
        write_to_pickle(f'{dst_dir}\\ids_{str(n_block).zfill(2)}.pkl', ids)
        ids = []
        n_block += 1

write_to_pickle(f'{dst_dir}\\ids_{str(n_block).zfill(2)}.pkl', ids)