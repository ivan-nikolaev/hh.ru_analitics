from project_tools.os_tools import generator_files_in_dir
import zipfile
import pickle

def extract_zip_by_vacancy(input_zipfile, n=-1):
    #print(f"\nОткрываем zip файл: {input_zipfile}")
    with zipfile.ZipFile(input_zipfile) as opened_zip:

        tmp_files = opened_zip.namelist()[:]
        tmp_files_ = tmp_files[:] if n==-1 else tmp_files[:n]

        #for pickle_file_in_zip in tqdm(tmp_files_, desc="files in zip"):
        for pickle_file_in_zip in tmp_files_:
            with opened_zip.open(pickle_file_in_zip, 'r') as mypicklefile:
                block_vacancies = pickle.load(mypicklefile)
                for vacancy in block_vacancies:
                    yield vacancy


def get_vacancies_from_dir_with_zips(dir_with_zips, first_n_files = -1):
    if(first_n_files == -1):
        files_zip = [file for file in generator_files_in_dir(dir_with_zips, extension='.zip')]
    else:
        files_zip = [file for file in generator_files_in_dir(dir_with_zips, extension='.zip')][:first_n_files]

    #print(files_zip)

    for file_zip in files_zip:
        for vacancy in extract_zip_by_vacancy(file_zip):
            yield vacancy


def get_specializations_list(vacancy_json):
    try:
        return [v['id'] for v in vacancy_json['specializations']]
    except:
        return []


def get_id_specs_areas_pub_create_infos(vacancy_json):
    vacancy = {}
    try:
        vacancy['id'] = vacancy_json['id']
    except:
        vacancy['id'] = None

    try:
        vacancy['specializations_ids'] = list(set([spec['id'] for spec in vacancy_json['specializations']]))
    except:
        vacancy['specializations_ids'] = []

    try:
        vacancy['profarea_ids'] = list(set([spec['profarea_id'] for spec in vacancy_json['specializations']]))
    except:
        vacancy['profarea_ids'] = []

    try:
        vacancy['published_at'] = vacancy_json['published_at']
    except:
        vacancy['published_at'] = None

    try:
        vacancy['created_at'] = vacancy_json['created_at']
    except:
        vacancy['created_at'] = None

    return vacancy