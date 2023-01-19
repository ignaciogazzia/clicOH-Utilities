import requests
import json


def search_packages(packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer tuTokenAquí"
    }
    sesion = requests.session()

    for pack in packages:
        url = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/?order_by=-id&section=list_packages&search=' + \
            pack + '&page=1&size=100'
        # url = 'http://ppointapi.clicoh.com/api/v1/pickup_points/packages/?search=' + \
        #    pack + '&section=list_packages'
        response = sesion.get(url=url, headers=headers)
        diccionario = json.loads(response.text)
        print("Paquete: " + pack + " ---> " + estaEnElSoft(diccionario))


def estaEnElSoft(respuesta: str):
    if respuesta["count"] == 1:
        return 'está en el soft'
    return 'no está en el soft/devolvió 2 o más paquetes'


if __name__ == '__main__':
    # fill the ids array with id packages (meli/clicoh)
    # format ids = ["id1", "id2", ....]
    packages = [
        "41927690888",
        "41927668735",
        "41927659101",
        "41927624472",
        "41927602893",
        "41927600792",
        "41927579272",
        "41927529448",
        "41927506158",
        "41927490795",
        "41927450643",
        "41927451122",
        "41927421931",
        "41927379980",
        "41927357467",
        "41927230037",
        "41927244758",
        "41927215990",
        "41927223281",
        "41927218280",
        "41927130329",
        "41927119893",
        "41927087357",
        "41927077155",
        "41927048912",
        "41926990538",
        "41926983185",
        "41926928115",
        "41926878649",
        "41926869996",
        "41926796694",

        "41928835798",
        "41928828377",
        "41928830916",
        "41928823811",
        "41928775901",
        "41928737575",
        "41928731286",
        "41928728765",
        "41928729446",
        "41928721207",
        "41928717859",
        "41928692235",
        "41928688686",
        "41928686015",
        "41928683917",
        "41928621606",
        "41928620198",
        "41928620225",
        "41928615442",
        "41928613983",
        "41928577803",
        "41928569001",
        "41928568821",
        "41928549546",
        "41928519960",
        "41928519472",
        "41928476411",
        "41928423394",
        "41928403458",
        "41928341074",
        "41928272621",
        "41928257537",
        "41928252307",
        "41928246558",
        "41928227952",
        "41928193972",
        "41928161589",
        "41928106526",
        "41928097105",
        "41928094832",
        "41928062531",
        "41928055229",
        "41928041712",
        "41928034362",
        "41927993765",
        "41927928020",
        "41927874328",
        "41927870423",
        "41927737249",
        "41927732639"

    ]
    search_packages(packages)
