from src.CRUD.mensajes import separacion, mensajeBienvenida, mensajeOpcion, mensajeElegido
from src.CRUD.inputs import inputOperacion, preguntarCantidad
from src.CRUD.read import unoOVariosRead
from src.CRUD.create import unoOVariosCreate
from src.CRUD.delete import unoOVariosDelete
from src.CRUD.update import unoOVariosUpdate

# Este módulo se va a encargar de reunir las cuatro principales funcionalidades del crud y
# y de generar una interfaz gráfica con la cual guiar al usuario en sus consultas.

opciones = {0:"Continuar con el programa",1:"Crear un documento",2:"Encontrar un documento",3:"Actualizar un documento",4:"Eliminar un documento",5:"Salir"}

# En primer lugar, se da la bienvenida y devuelve un input para elegir una operación
def bienvenidaCRUD():

    mensajeBienvenida()
    mensajeOpcion()

# Esta funcionalidad comprueba que operacion realizara el programa
def ejecucionOperacion(operacion):

    if int(operacion) == 0:

        mensajeElegido(opciones[0])
        preguntarCantidad()


    elif int(operacion) == 1:

        mensajeElegido(opciones[1])
        unoOVariosCreate(preguntarCantidad())


    elif int(operacion) == 2:

        mensajeElegido(opciones[2])
        unoOVariosRead(preguntarCantidad())


    elif int(operacion) == 3:

        mensajeElegido(opciones[3])
        unoOVariosUpdate(preguntarCantidad())


    elif int(operacion) == 4:

        mensajeElegido(opciones[4])
        unoOVariosDelete(preguntarCantidad())

    elif int(operacion) == 5:

        mensajeElegido(opciones[5])
        print("Cerrando el programa.")
        SystemExit



bienvenidaCRUD()
ejecucionOperacion(inputOperacion())