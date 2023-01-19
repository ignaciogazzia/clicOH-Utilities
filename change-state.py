import requests
import json


def search_packages(packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer tuTokenAquí"
    }
    sesion = requests.session()

    for pack in packages:
        # Conseguir el id del paquete
        url = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/?order_by=-id&section=list_packages&search=' + \
            pack + '&page=1&size=100'
        response = sesion.get(url=url, headers=headers)
        diccionario = json.loads(response.text)
        path = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/' + \
            str(diccionario['results'][0]['id']) + '/?edit=true'

        # Conseguir la info del paquete
        respuestaGET = json.loads(sesion.get(url=path, headers=headers).text)

        # Modificar el json que devuelve con lo que queremos modificar masivamente: (ej. extra_info)
        # Ejemplo: cambiar de estado
        respuestaGET["state"] = "returned_to_origin"

        # Mandatory changes before put method: (3) client_id, current_state_id y product_variant ids (set)
        # Para que soft acepte el PUT necesitamos hacer estos siguientes cambios:
        respuestaGET['client'] = respuestaGET['client']['id']
        respuestaGET['current_state'] = respuestaGET['current_state']['id']
        for variant in respuestaGET['packagedetail_set']:
            variant['product_variant'] = variant['product_variant']['id']

        # Actualizar los paquetes
        urlPUT = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/' + \
            str(diccionario['results'][0]['id']) + '/'
        respuestaPUT = sesion.put(
            url=urlPUT, headers=headers, json=respuestaGET)
        if (respuestaPUT.status_code == 200):
            print('Paquete: ', pack, ' modificado con exito! \n')
        else:
            print('Paquete: ', pack, ' NO MODIFICADO! \n\n')


if __name__ == '__main__':
    # fill the ids array with id packages (meli/clicoh)
    # format ids = ["id1", "id2", ....]
    packages = [
        "XPHZQ67093"
    ]

    search_packages(packages)
