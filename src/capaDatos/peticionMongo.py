import json
import requests
import os

# Este modulo se va a encargar de conseguir la petición de mongoDB

# Definimos en el entorno la variable de entorno MONGO_KEY que utilizaremos en la peticion. Por seguridad
def mongoKey():

    MONGO_KEY = os.environ['MONGO_KEY'] # Con el modulo os conseguimos llamar el valor de nuestra v. entorno

    return MONGO_KEY

# Definimos en el entorno la variable de entorno MONGO_URL que utilizaremos en la peticion. Por seguridad
def mongoUrl():

    MONGO_URL = os.environ['MONGO_URL'] # Con el modulo os conseguimos llamar el valor de nuestra v. entorno

    return MONGO_URL

# Esta función ejecuta la petición al servidor de mongoAtlas mediante la cual recibimos una respuesta
def conseguirRespuestaDatos(key,url):

    pipeline = [{ "$lookup": { "from": "rentals_data", "localField": "where._idrental",
    "foreignField": "_idrental", "as": "where" } },
    { "$project": { "_id": 0, "bikes._id": 0,"where._id":0} }
        ] # Esta variable es el filtro que utilizaremos para conseguir nuestra respuesta de mongoDB

    payload = json.dumps({
        "collection": "bikes_data",
        "database": "rentatorsl",
        "dataSource": "Cluster0",
        "pipeline":pipeline
    }) # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': key, 
    } # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    

    try: # Probamos que la respuesta se puede ejecutar sin problemas
        response = requests.request("POST", url, headers=headers, data=payload)    
        codigoRespuesta = response.status_code

        if codigoRespuesta == 200: # Comprobamos que el código enviado es el correcto y devolvemos el valor de la respuesta
            print("Conexion con el servidor establecida, respuesta recibida")
            return response

        else: # En caso de que no sea el código que necesitamos, enviamos una excepción
            raise ConnectionError("La conexión con el servidor ha fallado, vuelva a intentarlo en unos instantes")

    except: # En el caso de que no se consiga establecer la conexión con mongoDb se devuelve un error
        print("La conexión con el servidor ha tenido un problema, asegurese que los datos son correctos y vuelva a intentarlo.")