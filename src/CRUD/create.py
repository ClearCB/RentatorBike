from src.CRUD.actions import actionSintax, key
from src.CRUD.mensajes import separacion
import json
import requests
# En este modulo se van a definir todas las funcionalidades necesárias para ejecutar una consulta de
# creación de documentos en mongoDB, posteriormente, la uniremos a un programa principal que ejecutara
# una interfaz gráfica que nos será útil para guiar al usuario a ejecutar dichos comandos. 

# Esta funcion nos permitirá insertar un documento modelo en la base de datos
def createUnoMongoDB(documento):

    url = actionSintax("insertOne") # Url que determinara la acción ejecutada por mongo

    keyMongo = key() # Clave api de mongo

    payload = json.dumps({
        "collection": "bikes_data",
        "database": "rentatorsl",
        "dataSource": "Cluster0",
        "document": documento

    }) # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': keyMongo, 
    } # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    try: # Probamos que la respuesta se puede ejecutar sin problemas
        response = requests.request("POST", url, headers=headers, data=payload)    
        codigoRespuesta = response.status_code

        if codigoRespuesta == 201: # Comprobamos que el código enviado es el correcto y devolvemos el valor de la respuesta.  201 = insercion correcta

            print("Conexion con el servidor establecida, respuesta recibida")
            response = response.text
            separacion()
            print("El documento con el id: ", response, " ha sido insertado correctamente.")
            separacion()

        else: # En caso de que no sea el código que necesitamos, enviamos una excepción
            print("La conexión con el servidor ha fallado, vuelva a intentarlo en unos instantes")
            raise ConnectionError

    except: # En el caso de que no se consiga establecer la conexión con mongoDb se devuelve un error
        print("La conexión con el servidor ha tenido un problema, asegurese que los datos son correctos y vuelva a intentarlo.")
        

# Esta funcion nos permitirá insertar varios documento modelo en la base de datos
def createVariosMongoDB(documentos):

    url = actionSintax("insertMany") # Url que determinara la acción ejecutada por mongo

    keyMongo = key() # Clave api de mongo

    payload = json.dumps({
        "collection": "bikes_data",
        "database": "rentatorsl",
        "dataSource": "Cluster0",
        "documents": documentos

    }) # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': keyMongo, 
    } # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    try: # Probamos que la respuesta se puede ejecutar sin problemas
        response = requests.request("POST", url, headers=headers, data=payload)    
        codigoRespuesta = response.status_code

        if codigoRespuesta == 201: # Comprobamos que el código enviado es el correcto y devolvemos el valor de la respuesta.  201 = insercion correcta

            print("Conexion con el servidor establecida, respuesta recibida")
            response = response.text
            separacion()
            print("Los documentos documentos con el id: ", response, " han sido insertados correctamente.")
            separacion()

        else: # En caso de que no sea el código que necesitamos, enviamos una excepción
            print("La conexión con el servidor ha fallado, vuelva a intentarlo en unos instantes")
            raise ConnectionError

    except: # En el caso de que no se consiga establecer la conexión con mongoDb se devuelve un error
        print("La conexión con el servidor ha tenido un problema, asegurese que los datos son correctos y vuelva a intentarlo.")