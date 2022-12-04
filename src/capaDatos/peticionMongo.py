import json
import requests
import os


# Este modulo se va a encargar de conseguir la petición de mongoDB. En primer lugar 
# añadiremos en nuestras variables de entorno la api-key por motivos de seguridad, después
# la función ejecutara la petición al servidor de mongoDB y comprobaremos que la petición es 
# la necesária para continuar con la ejecución del programa.


# Aqui estamos solicitando el valor de la uri/api-key de nuestro entorno 

def mongoKey():

    MONGO_KEY = os.environ['MONGO_KEY']

    return MONGO_KEY

# Aqui estamos solicitando el valor de la url/peticio de nuestro entorno 

def mongoUrl():

    MONGO_URL = os.environ['MONGO_URL']

    return MONGO_URL

# Esta función ejecuta la petición al servidor de mongoAtlas mediante la cual recibimos una respuesta.

def conseguirRespuestaDatos(key,url):

    pipeline = [{ "$lookup": { "from": "rentals_data", "localField": "where._idrental",
    "foreignField": "_idrental", "as": "where" } },
    { "$project": { "_id": 0, "bikes._id": 0,"where._id":0,"where.bikes":0} }
        ]

    payload = json.dumps({
        "collection": "bikes_data",
        "database": "rentatorsl",
        "dataSource": "Cluster0",
        "pipeline":pipeline
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': key, 
    }

    

    try:
        response = requests.request("POST", url, headers=headers, data=payload)    
        codigoRespuesta = response.status_code

        if codigoRespuesta == 200:
            print("Conexion con el servidor establecida, respuesta recibida")
            return response

        else:
            raise ConnectionError("La conexión con el servidor ha fallado, vuelva a intentarlo en unos instantes")

    except:
        print("La conexión con el servidor ha tenido un problema, asegurese que los datos son correctos y vuelva a intentarlo.")