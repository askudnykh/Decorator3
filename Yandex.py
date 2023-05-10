import requests

class Yandex:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_url(self, name_file, url_file):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": "reserve/" + name_file, "url": url_file}
        response = requests.post(url, headers=headers, params=params)
        if response.status_code == 202:
            print(f"Файл {name_file} загружен")

    def meta_data(self, params="/"):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": params}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def create_folder(self, name):
        name_folder = name
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": name_folder}
        response = requests.put(url, headers=headers, params=params)

    def check_folder(self, new_folder='reserve'):
        list_file = self.meta_data()['_embedded']['items']
        folder = [True for x in list_file if x['name'] == new_folder]
        if folder != [True]:
            self.create_folder(new_folder)
            print(f"Создана папка {new_folder} для резервного копирования")
        else:
            print(f"Резервное копирование осуществленно в существующую папку {new_folder}")
