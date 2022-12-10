# En este modulo vamos a implementar todos los inputs que vamos a necesitar
# en el módulo crud y sus funcionalidades

# Esta funcion define la operacion que va a ejecutar el programa
def inputOperacion():

    operacion = input("Escribe un número del 0 al 5: ")
    return operacion

# Esta funcion pregunta al usuario con cuantos documentos quiere interactuar con mongo
def preguntarCantidad():

    cantidad = input("¿Con cuantos documentos quieres interactuar? Uno o varios: ")
    return cantidad


