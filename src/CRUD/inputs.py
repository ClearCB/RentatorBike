import time
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
def rellenarDocumentosCrear(cantidad):


    time.sleep(0.2)
    if cantidad.lower() == "uno":

        print('''
    Introduce ahora el documento que quieres introducir
    en la base de datos''')

        time.sleep(0.3)
        idBike = input("Escribe el identificador de la bicicleta con el siguiente formato [MA0101]: ")
        estado = input("Escribe el estado de la bicicleta: ")
        tipo = input("Escribe el tipo de la bicicleta: ")
        groupset = input("Escribe el groupset: ")
        tamaño = input("Escribe el tamaño del marco: ")
        ruedas = input("Escribe el tamaño de las ruedas: ")
        marca = input("Escribe la marca: ")
        complementos = input("Escribe los complementos con el siguiente formato (sillita de bebe','casco','bomba): ")
        precio = input("Escribe el precio por día de la bicicleta: ")
        ubicacion = input("Escribe la ubicación de la bicicleta con el siguiente formato [MA01]: ")
        imagen = input("Escribe la direccion de la imagen: ")

        documento = { "_idbike": idBike,
        "state": estado,
        "type": tipo,
        "techinfo": { "groupset": groupset, "size": tamaño, "wheels": ruedas, "brand": marca },
        "complements": ['"',complementos,'"'],
        "prize_euros_days": precio,
        "where": { "_idrental": ubicacion },
        "img": imagen
    }

        return documento

    elif cantidad.lower() == "varios":

        documentos = []
        cuantas = input("Cuantas bicicletas quieres insertar: ")
        cuenta = 0
        print('''
Introduce ahora el documento que quieres introducir
en la base de datos''')
        while cuenta != int(cuantas):
            
            time.sleep(0.3)
            idBike = input("Escribe el identificador de la bicicleta con el siguiente formato [MA0101]: ")
            estado = input("Escribe el estado de la bicicleta: ")
            tipo = input("Escribe el tipo de la bicicleta: ")
            groupset = input("Escribe el groupset: ")
            tamaño = input("Escribe el tamaño del marco: ")
            ruedas = input("Escribe el tamaño de las ruedas: ")
            marca = input("Escribe la marca: ")
            complementos = input("Escribe los complementos con el siguiente formato (sillita de bebe','casco','bomba): ")
            precio = input("Escribe el precio por día de la bicicleta: ")
            ubicacion = input("Escribe la ubicación de la bicicleta con el siguiente formato [MA01]: ")
            imagen = input("Escribe la direccion de la imagen: ")

            documento = { "_idbike": idBike,
            "state": estado,
            "type": tipo,
            "techinfo": { "groupset": groupset, "size": tamaño, "wheels": ruedas, "brand": marca },
            "complements": ["'",complementos,"'"],
            "prize_euros_days": precio,
            "where": { "_idrental": ubicacion },
            "img": imagen
        }
            cuenta +=1
            documentos.append(documento)
        return documentos

# Esta funcion nos pedirá la identificación de la bicicleta que el usuario quiere buscar
def identificadorBici():
    
    idBici = input("¿Quieres introducir el identificador de la bicicleta? Y/N   ")

    if idBici.lower() == "y":

        time.sleep(0.5)
        print('''
    Escribe el identificador de la bicicleta
    que quieres visualizar con el siguiente
    formato: [MA,PA,SO,CA,AL]+[01,02]+[01,02].

    Debería de verse algo así PA0101.''')

        time.sleep(0.5)
        print('''
    Primero elige la zona del renta bike.
    Elige alguna de las siguientes zonas:

    MA(manacor), PA(palma), SO(soller), AL(alcudia) O CA(calvia)''')
        zona=input("Zona: ")

        print("Ahora selecciona un rental: escribe 01 O 02")
        rental=input("Rental: ")

        print("Por ultimo, seleciona una bici: 01 o 02")
        bici=input("Bici: ")

        identificador = zona+rental+bici
        return identificador

    else:
        pass
    
# Esta funcion nos devolverá el campo que se quiere modificar del documentos seleccionado
def elegirCampo():

    time.sleep(1)
    print('''
Escribe el campo que quieres modificar:

identificador, estado, precio, ubicacion, imagen
''')
    campo = input("Campo: ")

    if campo == "identificador":
        return "_idbike"

    if campo == "estado":
        return "state"

    if campo == "precio":
        return "prize_euros_days"

    if campo == "ubicacion":
        return "where._idrental"

    if campo == "imagen":
        return "img"


def elegirCambio():

    time.sleep(0.5)
    print('''
Escribe el cambio que deseas hacer

''')

    return input("Cambio: ")