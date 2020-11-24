import json


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print("====================================================================================")
        print(json.dumps(json.loads(json_thing, encoding='utf-8'), sort_keys=sort, indent=indents, ensure_ascii=False))
    else:
        print("====================================================================================")
        print(json.dumps(json_thing, sort_keys=sort, indent=indents, ensure_ascii=False))
    return None


def read_json_from_file(filename):
    with open(filename, 'r') as outfile:
        json_string = outfile.read()
        json_ = json.loads(json_string)
        return json_


def write_json_to_file(filename, json_):
    with open(filename, 'w') as outfile:
        text = json.dumps(json_, ensure_ascii=False)
        # print(type(text))
        try:
            outfile.write(text)
        except Exception:
            print("ошибка записи в файл")