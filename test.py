#%%
from project_tools.pickle_tools import read_from_pickle


file_new = r"F:\!hh.ru\vacancies_pickle_all_add\downloading\00000000_00010000.pickle"
file_old = r"F:\!hh.ru\vacancies_pickle_all\00000000_01000000\00000000_00010000.pickle"


data_new = read_from_pickle(file_new)
data_old = read_from_pickle(file_old)

#%%

print(len(data_new), len(data_old))

#%%
for v in data_old[1000:1010]:
    print(v)

