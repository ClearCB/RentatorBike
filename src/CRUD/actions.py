# En este módulo vamos a definir todas las variables de entorno necesárias para 
# conseguir las acciones del modulo CRUD
import os

# Variable API-key que nos permite conectarnos a la base de datos como administradores
def key():

    try:
        MONGO_KEY = os.environ['MONGO_KEY']
    except KeyError:
        print("La variable de entorno MONGO_KEY no se ha podido encontrar. Por favor, corrige el error y vuelve a intentarlo")
    
    return MONGO_KEY

# Variable que contiene la url de accion de lectura
def actionSintax(action):

    try:
        MONGO_ACTION = os.environ['MONGO_ACTION']
    except KeyError:
        print("La variable de entorno MONGO_ACTION no se ha podido encontrar, por favor, corrige el error y vuelve a intentarlo")
    
    MONGO_ACTION += action

    return MONGO_ACTION

