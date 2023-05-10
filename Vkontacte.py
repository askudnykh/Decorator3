import requests

class Vkontacte:
    def __init__(self, token: str):
        self.token = token
        self.V = "5.131"
        self.URL = "https://api.vk.com/method/"

    def photo(self, id: str):
        params = {
            "owner_id": id,
            "extended": '1',
            "album_id":'profile',
            "access_token": self.token,
            "count": 5,
            "v": self.V
            }
        url_1 = "https://api.vk.com/method/photos.get"
        res = requests.get(url_1, params=params)
        return res.json()

    def list_avatar(self, id):
        avatar = self.photo(id)
        list_avatar = {}
        list_avatar["list_avatar"] = []
        for jpg in avatar["response"]["items"]:
            dict = {}
            dict["like"] = str(jpg["likes"]["count"])
            dict["size"] = jpg["sizes"][-1]['type']
            dict["url"] = jpg["sizes"][-1]['url']
            dict["date"] = str(jpg["date"])
            list_avatar["list_avatar"].append(dict)
        return list_avatar
