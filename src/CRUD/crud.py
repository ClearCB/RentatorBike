from src.CRUD.mensajes import separacion, mensajeBienvenida, mensajeOpcion, mensajeElegido, mensajeRellenarInfo
from src.CRUD.inputs import inputOperacion, preguntarCantidad, rellenarDocumentosCrear, identificadorBici, elegirCambio, elegirCampo
from src.CRUD.read import unoOVariosRead
from src.CRUD.create import unoOVariosCreate
from src.CRUD.delete import unoOVariosDelete
from src.CRUD.update import unoOVariosUpdate
import sys

# Este módulo se va a encargar de reunir las cuatro principales funcionalidades del crud y
# y de generar una interfaz gráfica con la cual guiar al usuario en sus consultas.

opciones = {0:"Continuar con el programa",1:"Crear un documento",2:"Encontrar un documento",3:"Actualizar un documento",4:"Eliminar un documento",5:"Salir"}

# En primer lugar, se da la bienvenida y devuelve un input para elegir una operación
def bienvenidaCRUD():

    mensajeBienvenida()

# Esta funcionalidad comprueba que operacion realizara el programa
def ejecucionOperacion(operacion):


    if int(operacion) == 0:

        mensajeElegido(opciones[0])
        print("Continuando con la generación de páginas estáticas")

    elif int(operacion) == 1:

        mensajeElegido(opciones[1])
        mensajeRellenarInfo()
        cantidad = preguntarCantidad()
        unoOVariosCreate(cantidad,rellenarDocumentosCrear(cantidad))


    elif int(operacion) == 2:

        mensajeElegido(opciones[2])
        mensajeRellenarInfo()
        unoOVariosRead(preguntarCantidad(),identificadorBici())


    elif int(operacion) == 3:

        mensajeElegido(opciones[3])
        mensajeRellenarInfo()
        unoOVariosUpdate(preguntarCantidad(),identificadorBici(), elegirCampo(), elegirCambio())


    elif int(operacion) == 4:

        mensajeElegido(opciones[4])
        mensajeRellenarInfo()
        unoOVariosDelete(preguntarCantidad(), identificadorBici())

    elif int(operacion) == 5:

        mensajeElegido(opciones[5])
        print("Cerrando el programa.")
        separacion()
        sys.exit()

    return int(operacion)
        

# Esta funcionalidad permite al usuario elegir una operación
def elegirFunción():

    mensajeOpcion()
    funcion = ejecucionOperacion(inputOperacion())

    if funcion == 0:
        return None
    
    if funcion == 5:
        sys.exit()

    mensajeOpcion()
    while ejecucionOperacion(inputOperacion()) != 0:
        mensajeOpcion()

# Esta es la función principal del CRUD
def CRUD():

    bienvenidaCRUD()
    elegirFunción()