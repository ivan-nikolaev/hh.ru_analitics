#%%
import os
from tqdm import tqdm
import zipfile
import shutil
from project_tools.os_tools import generator_files_in_dir
#%%
project_dir = r"F:\!hh.ru"

src_dir = f"{project_dir}\\vacancies_pickle_all"
dst_dir = f"{project_dir}\\vacancies_pickle_all_zip"

if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
os.mkdir(dst_dir)

files = [filename for filename in generator_files_in_dir(src_dir)]

print(len(files))

#%%
for filename_pkl in tqdm(files[:]):
    sub_dir = '\\'.join(filename_pkl.split('\\')[:-1]).replace(src_dir, dst_dir)
    print(sub_dir)
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)

    filename_zip = filename_pkl.replace(src_dir, dst_dir).replace('.pickle', '.zip')
    if not os.path.exists(filename_zip):
        with zipfile.ZipFile(filename_zip, 'w', zipfile.ZIP_DEFLATED) as myzip:
            myzip.write(filename_pkl, os.path.basename(filename_pkl))

#os.remove(filename_pkl)