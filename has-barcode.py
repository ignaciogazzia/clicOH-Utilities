import requests
import json
from nltk.tokenize import word_tokenize
import time


def look_for_barcode(id_packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer ..."
    }
    sesion = requests.session()
    ids = []
    for pack in id_packages:
        url = f'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/{pack}/'

        response = sesion.get(url=url, headers=headers)
        diccionario = json.loads(response.text)

        print(f'Paquete {pack} con barcode') if len(
            diccionario["bar_code"]) > 1 else print(f'Paquete {pack} SIN barcode')


if __name__ == '__main__':
    id_packages = [1263745, 1263879, 1263869, 1263893, 1263952, 1263748, 1263913, 1263741,
                   1263833, 1263910, 1263788, 1263732, 1263936, 1263810, 1263851, 1263758, 1263724]

    look_for_barcode(id_packages)
