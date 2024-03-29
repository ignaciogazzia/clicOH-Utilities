import requests
import json
from nltk.tokenize import word_tokenize
import time


def search_packages(packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer tuTokenAquí"
    }
    sesion = requests.session()

    for pack in packages:

        url = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/?order_by=-id&section=list_packages&search=' + \
            pack + '&page=1&size=100'

        response = sesion.get(url=url, headers=headers)
        diccionario = json.loads(response.text)

        if diccionario["count"] == 1:
            try:
                print('Paquete: ', pack, 'con WH: ',
                      diccionario['results'][0]['warehouse2']['name'])
            except:
                print('* Paquete: ', pack, 'con WH: ',
                      diccionario['results'][0]['warehouse']['name'])


def estaEnElSoft(respuesta: str, codigo: str):
    if respuesta["count"] == 1:
        print('Paquete: ', codigo, 'con WH: ',
              respuesta['results'][0]['warehouse2']['name'])
        return
        # return 'está en el soft'
    return 'no está en el soft/devolvió 2 o más paquetes'


if __name__ == '__main__':
    # fill the ids array with id packages (meli/clicoh)
    # format ids = ["id1", "id2", ....]
    packages = ["WNHFM63012",
                "FMANP28493",
                "RIGVH80153",
                "IFDCZ41927",
                "VMIOJ10587",
                "POBGM54827",
                "KBNMF71049",
                "OARTB32180",
                "SKOHQ08521",
                "RHUQL76951",
                "IJTZN24079",
                "UDAYC27538",
                "NOGCJ58942",
                "EZRTB16073",
                "HBWRK46839",
                "YPNGB47301",
                "JETPV74932",
                "NRXSV87921",
                "FWCPD80379",
                "HSYJT79580",
                "ORXJZ23450",
                "MHAXO38071",
                "GUNCJ25784",
                "PQXBE12379",
                "AVDKB84539",
                "VLCWP48053",
                "NVQRE38652",
                "VLQOK72541",
                "JDNWH20579",
                "YVKOE09874",
                "UBXVN32691",
                "QCJBE32519",
                "QXZPT52097",
                "DQFPY28956",
                "QJRXD74608",
                "MURLV06958",
                "DCEGO03259",
                "MABRP19825",
                "PHBCR93584",
                "OXWYT14265",
                "EAWJZ61752",
                "SKIVR31654",
                "TPQCD37254",
                "VPGSQ26573",
                "TPJAM27016",
                "WKSNC85214",
                "FJKLX05368",
                "QXALW07245",
                "QXALW07245",
                "UDAVO02863",
                "IDFAQ49781",
                "ZAHOC03982",
                "JDNZC89062",
                "THRFZ92516",
                "LUABK29075",
                "NYIUO95386",
                "TPKUX04713",
                "FLCRX28519",
                "JYOKF18946",
                "MDBGC57193",
                "UBXQD86970",
                "KGDZO15739",
                "BGPNY54130",
                "ESQAI75231",
                "AWCKO51823",
                "vzmcd37490",
                "bxtsk79420",
                "zckod30928",
                "xhosu59762",
                "bleuq60841",
                "ujeds52649",
                "idejn64350",
                "kpxtr71309",
                "bfxah51867",
                "eqgns03254",
                "oqlrf46178",
                "jrpnc61283",
                "vxpct59048",
                "alkvd87154",
                "jgqke43590",
                "fxpyk74029",
                "qfynr57893",
                "pbewx86031",
                "NEKIS85471",
                "jaieu01362",
                "zwpym78541",
                "ijtzn24079",
                "wfbuv32107",
                "mibsf35960",
                "bomch80241",
                "nkqjb40967",
                "nkqjb40967",
                "pxvbt10572",
                "hefko73594",
                "kofwr10543",
                "miohu14903",
                "wmuzt40569",
                "raumc49265",
                "ypazm64031",
                "cngiw81654",
                "kqsjz65721",
                "mhwli03914",
                "pniez35498",
                "ceakd94306",
                "ltanp15968",
                "pbawe15492",
                "zoigt70341",
                "qvaho12480",
                "nfums58309",
                "vsxbo39647",
                "nvyci09184",
                "dfvtc43781",
                "ywqxh40529",
                "vhald05762",
                "vyloq84125",
                "afrjm92160",
                "xuhgo43671",
                "bomxl16497",
                "xikft96852",
                "fjabc08693",
                "AQKYC27685",
                "XKYND98610"]

    search_packages(packages)
