

#%%
from project_tools.vacancies_tools import get_vacancies_from_dir_with_zips
from tqdm import tqdm
#%%
src_dir = r"F:\!hh.ru\vacancies_pickle_all_zip"
add_dir = r"F:\!hh.ru\vacancies_pickle_all_zip_add"
#%%
ids = []

for vacancy in tqdm(get_vacancies_from_dir_with_zips(src_dir)):
    #print(vacancy['id'])
    ids.append((vacancy['id']))


ids_add = []
for vacancy in tqdm(get_vacancies_from_dir_with_zips(add_dir)):
    #print(vacancy)
    ids_add.append((vacancy['id']))

print(len(ids), len(ids_add))

#%%