import requests
import json
from nltk.tokenize import word_tokenize
import time

headers = {
    "Content-Type": "application/json",
    "authorization": "Bearer ..."
}


def delete_products(products: list):
    sesion = requests.session()
    for prod in products:
        url = f'https://release--api.clicoh.com/api/v1/pickup_points/products/{prod}/'
        response = sesion.delete(url=url, headers=headers)
        if response.status_code == 204:
            print(f'\nProducto {prod} eliminado con éxito!\n')
            break
        print(
            f'\nHubo error al intentar eliminar {prod} ---> Cod {response.status_code}{response.reason}\n')


if __name__ == '__main__':
    products = [
        "1918233"
    ]

    delete_products(products)
