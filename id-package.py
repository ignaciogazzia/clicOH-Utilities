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
        "TD1036804314",
        "TX1036804313",
        "TC1036804312",
        "TS1036804310",
        "TZ1036804305",
        "TH1036804303",
        "TR1036804302",
        "TH1036804301",
        "TV1036814214",
        "TS1036814209",
        "TA1036814208",
        "TG1036814207",
        "TL1036814205",
        "TZ1036811803",
        "TW1036811801",
        "TX1036811207",
        "TE1036811205",
        "TC1036803602",
        "TK1036803601",
        "TE1036814213",
        "TM1036814211",
        "TJ1036814203",
        "TV1036814202",
        "TX1036814201",
        "TR1036811811",
        "TW1036811810",
        "TS1036811809",
        "TX1036811807",
        "TJ1036811806",
        "TZ1036811805",
        "TB1036811802",
        "TZ1036811214",
        "TG1036811213",
        "TE1036811212",
        "TO1036811210",
        "TO1036811208",
        "TL1036811203",
        "TX1036811202",
        "TP1036811201",
        "TH1036803614",
        "TB1036803613",
        "TK1036803612",
        "TL1036803610",
        "TA1036803608",
        "TZ1036803605",
        "TS1036803603",
        "TH1036803607"
    ]

    search_packages(packages)
