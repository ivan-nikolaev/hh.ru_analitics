#%%
from project_tools.pickle_tools import read_from_pickle


#file_new = r"F:\!hh.ru\vacancies_pickle_all_add\downloading\00000000_00010000.pickle"
#file_old = r"F:\!hh.ru\vacancies_pickle_all\00000000_01000000\00000000_00010000.pickle"

file_new = r"C:\Users\Ivan\Downloads\00000000_00010000_new.pkl"
file_old = r"C:\Users\Ivan\Downloads\00000000_00010000_old.pickle"


data_new = read_from_pickle(file_new)
data_old = read_from_pickle(file_old)

#%%

print(len(data_new), len(data_old))

#%%
ids_old = [v['id'] for v in data_old]
ids_new = [v['id'] for v in data_new]


print(len(ids_new), len(ids_old))

dif = [id for id in ids_old if id not in ids_new]
print(dif)

#%%
data_old_dif = [v for v in data_old if v['id'] in dif]

for v in data_old_dif:
    print(v)