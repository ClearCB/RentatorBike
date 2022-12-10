# En este modulo vamos a implementar todos los mensajes predeterminados que van a aparecer en la consola.

# Printara una separación entre secciones en la consola.
def separacion():

    separacion = "\n--------------------------------------------------------------\n"

    print(separacion)

# Este será el mensaje de bienvenida cuando se ejecute el programa
def mensajeBienvenida():

    bienvenida = '''
Bienvenido al módulo CRUD.

Vamos a indicarte las instrucciones necesarias para poder 
realizar las operaciones CREATE, READ, UPADTE y DELETE 
en nuestra base de datos. \n'''

    print(bienvenida)
