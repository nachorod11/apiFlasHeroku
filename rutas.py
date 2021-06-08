# Importamos librerías
import pandas as pd
import json

dfdir = pd.read_csv('data/direcciones.csv')
dfchar = pd.read_csv('data/puntosCarga.csv')

# Convierto a diccionario (y luego json) esta línea
def dataframe_to_json(row):
    columnas = ['ID', 'Title', 'AddressLine1', 'Town', 'Postcode', 'Latitude', 'Longitude', 'ContactTelephone1']
    data = row[columnas]
    data_dict = data.to_dict('list')
    json_ = json.dumps(data_dict)
    return json_

# Ruta 1
infoOrigen1 = dataframe_to_json(dfdir[dfdir.ID==9389])
infoDestino1 = dataframe_to_json(dfdir[dfdir.ID==168388])
infoCarga11 = dataframe_to_json(dfdir[dfdir.ID==165453])
infoCarga21 = dataframe_to_json(dfdir[dfdir.ID==162406])

# Ruta 2
infoOrigen2 = dataframe_to_json(dfdir[dfdir.ID==9389])
infoDestino2 = dataframe_to_json(dfdir[dfdir.ID==168388])
infoCarga12 = dataframe_to_json(dfdir[dfdir.ID==97539])
infoCarga22 = dataframe_to_json(dfdir[dfdir.ID==61421])

rutas = [{'id': 0,
         'info_origen': infoOrigen1,
         'destino': infoDestino1,
         'distancia': '539 km',
         'carga1': infoCarga11,
         'carga2': infoCarga21},
         {'id':1,
             'origen': infoOrigen2,
             'destino': infoDestino2,
             'distancia': '562 km',
             'carga1': infoCarga12,
             'carga2':infoCarga22}]