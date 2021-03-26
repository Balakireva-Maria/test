import requests
token = 'OAuth AQAAAABTfFIlAADLW6wJrBu-qEJ8o-bG61H5rlg'
def create_folder(folder_name):
    r = requests.put(''.join(['https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F',folder_name]),
                headers={'Authorization': token},
                 )
    return r




