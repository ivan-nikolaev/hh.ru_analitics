
#%%
from project_tools.os_tools import generator_files_in_dir
import shutil
import os
from pathlib import Path
from tqdm import tqdm

src = 'vacancies_pickle'
dsr = src+'_add'
project_dir = f"F:\\!hh.ru\\{src}"

for f in tqdm(generator_files_in_dir(project_dir)):
    if f.find("_add")>=0:
        #print(f)
        dst_dir = '\\'.join(f.replace(src, dsr).split('\\')[:-1])
        if(os.path.exists(dst_dir)==False):
            os.mkdir(dst_dir)
        Path(f).rename(f.replace(src, dsr))