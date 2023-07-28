import Vkontacte
import Yandex
import json
from progress.bar import IncrementalBar
from tools import logger

path = 'log1.txt'
@logger(path)
def list_dict2_json(name, size):
    dict = {"file_name": name, "size": size}
    return dict
@logger(path)
def new_name(old, new):
    if new != []:
        return new[0]
    else:
        return old
@logger(path)
def name_date_list(list, key_date, key_like, out_key):
    re_name_file = [(x[key_like] + '_' + out_key[key_date]) for x in list if x[key_like] == out_key[key_like] and x[key_date] != out_key[key_date]]
    name_file = (new_name(out_key[key_like], re_name_file)) + ".jpg"
    return name_file
@logger(path)
def new_json(name_json, dump_obj):
    with open(name_json, "w+") as file:
        json.dump(dump_obj, file, ensure_ascii=False, indent=2)

TOKEN_vk = ""
TOKEN_yd = ""
id_vk = "1"

vk = Vkontacte.Vkontacte(TOKEN_vk)
list_avatar = vk.list_avatar(id_vk)
avatars = list_avatar['list_avatar']
yandex = Yandex.Yandex(TOKEN_yd)
yandex.check_folder()

def reserved(avatars, count_max=5):
    bar = IncrementalBar('Progress', max = count_max)
    count = 0
    list_json = []
    for y in avatars:
        bar.next()
        name_file = name_date_list(avatars, 'date', 'like', y)
        dict = list_dict2_json(name_file, y['size'])
        list_json.append(dict)
        yandex.upload_url(name_file, y['url'])
        count += 1
        if count == count_max:
            break
    new_json("result.json", list_json)
    bar.finish()

reserved(avatars)