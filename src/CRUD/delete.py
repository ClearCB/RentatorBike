from src.CRUD.actions import actionSintax, key
from src.CRUD.mensajes import separacion
import json
import requests
# En este modulo se van a definir todas las funcionalidades necesárias para ejecutar una consulta de
# eliminación de documentos en mongoDB, posteriormente, la uniremos a un programa principal que ejecutara
# una interfaz gráfica que nos será útil para guiar al usuario a ejecutar dichos comandos. 

# Esta función se encargará de encontrar una bicicleta en concreto y eliminarla
def deleteUnoMongoDB(inputId):

    url = actionSintax("deleteOne") # Url que determinara la acción ejecutada por mongo

    keyMongo = key() # Clave api de mongo
    
    filter = {"_idbike":inputId}

    payload = json.dumps({
        "collection": "bikes_data",
        "database": "rentatorsl",
        "dataSource": "Cluster0",
        "filter": filter
    }) # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': keyMongo, 
    } # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    try: # Probamos que la respuesta se puede ejecutar sin problemas
        response = requests.request("POST", url, headers=headers, data=payload)    
        codigoRespuesta = response.status_code

        if codigoRespuesta == 200: # Comprobamos que el código enviado es el correcto y devolvemos el valor de la respuesta. 200 = eliminacion ejecutada correctamente

            print("Conexion con el servidor establecida, respuesta recibida")
            response = response.text
            response = json.loads(response)
            separacion()
            print("Se ha eliminado el documento con id '", inputId, "' correctamente")
            separacion()

        else: # En caso de que no sea el código que necesitamos, enviamos una excepción
            raise ConnectionError("La conexión con el servidor ha fallado, vuelva a intentarlo en unos instantes")

    except: # En el caso de que no se consiga establecer la conexión con mongoDb se devuelve un error
        print("La conexión con el servidor ha tenido un problema, asegurese que los datos son correctos y vuelva a intentarlo.")

# Esta función se encargará de encontrar varias bicicletas y eliminarlas
def deleteVariosMongoDB(inputId):

    url = actionSintax("deleteMany") # Url que determinara la acción ejecutada por mongo

    keyMongo = key() # Clave api de mongo
    
    filter = {"_idbike":inputId}

    payload = json.dumps({
        "collection": "bikes_data",
        "database": "rentatorsl",
        "dataSource": "Cluster0",
        "filter": filter
    }) # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': keyMongo, 
    } # Esta variable es en la cual introducimos toda la información que va a ser utilizada por mongo para devolvernos la respuesta

    try: # Probamos que la respuesta se puede ejecutar sin problemas
        response = requests.request("POST", url, headers=headers, data=payload)    
        codigoRespuesta = response.status_code

        if codigoRespuesta == 200: # Comprobamos que el código enviado es el correcto y devolvemos el valor de la respuesta. 200 = eliminacion ejecutada correctamente

            print("Conexion con el servidor establecida, respuesta recibida")
            response = response.text
            response = json.loads(response)
            separacion()
            print("Se han eliminado", response["deletedCount"],"documentos correctamente")
            separacion()

        else: # En caso de que no sea el código que necesitamos, enviamos una excepción
            raise ConnectionError("La conexión con el servidor ha fallado, vuelva a intentarlo en unos instantes")

    except: # En el caso de que no se consiga establecer la conexión con mongoDb se devuelve un error
        print("La conexión con el servidor ha tenido un problema, asegurese que los datos son correctos y vuelva a intentarlo.")