import requests
import json
from nltk.tokenize import word_tokenize
import time


def search_packages(packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer ..."
    }
    sesion = requests.session()
    ids = []
    for pack in packages:
        url = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/?order_by=-id&section=list_packages&search=' + \
            pack + '&page=1&size=100'
        response = sesion.get(url=url, headers=headers)
        diccionario = json.loads(response.text)
        ids.append(diccionario['results'][0]['id'])
        print('Paquete: ', pack, 'con id: ', diccionario['results'][0]['id'])

    print(ids)


if __name__ == '__main__':
    packages = [
        "IRZFQ06795",
        "IWJKO28057",
        "TANSJ71294",
        "ZNBWX28614",
        "TJCMH17689",
        "GQNAW61793",
        "XFJGC94672",
        "RETCK12689",
        "JFIBE92316",
        "NTVDS70349",
        "TIJCW62937",
        "SPZUK83125",
        "ZYIOB79251",
        "DPEFM96071",
        "SKXFV93758",
        "SJTQL05789",
        "QZRGS70198",
    ]

    search_packages(packages)
