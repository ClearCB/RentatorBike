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

# Esta funcion nos devolverá el/los documento/s que se insertará/n en la base de datos
def rellenarDocumentosCrear():

    print("Que bici quieres")

# Esta funcion nos pedirá la identificación de la bicicleta que el usuario quiere buscar
def identificadorBici():

    print("Que bici quieres")

# Esta funcion nos devolverá el campo y la modificación que se hará a los documentos seleccionados
def actualizarCampo():

    print("Que bici quieres")
