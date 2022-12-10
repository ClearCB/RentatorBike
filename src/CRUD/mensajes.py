import time
# En este modulo vamos a implementar todos los mensajes predeterminados que van a aparecer en la consola.

# Printara una separación entre secciones en la consola.
def separacion():

    separacion = "\n--------------------------------------------------------------\n"

    print(separacion)

# Este será el mensaje de bienvenida cuando se ejecute el programa
def mensajeBienvenida():

    separacion()
    bienvenida = '''
Bienvenido al módulo CRUD.
'''
    print(bienvenida)

    bienvenida = '''
Vamos a indicarte las instrucciones necesarias para poder 
realizar las operaciones CREATE, READ, UPDATE y DELETE 
en nuestra base de datos. \n'''

    time.sleep(1)
    print(bienvenida)
    separacion()

# Este mensaje da las opciones posibles al usuario
def mensajeOpcion():

    elegir = '''
Primero elige qué quieres hacer:

0- Continuar con el programa
1- Crear un documento
2- Encontrar un documento
3- Actualizar un documento
4- Eliminar un documento
5- Salir'''

    time.sleep(2)
    print(elegir)
    separacion()

# Este mensaje enseña al usuario que funcion ha elegido
def mensajeElegido(opcion):

    eleccion = f'''
Has seleccionado {opcion}. 
'''
    print(eleccion)


