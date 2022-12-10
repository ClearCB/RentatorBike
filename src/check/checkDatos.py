# Este modulo se va a dedicar a comprobar y poner una "barricada" en la capa de datos
# comprobando que la respuesta de mongo llega correctamente y que los documentos
# que se crean son modelo para que se ejecute el programa correctamente.

# Capturamos todos los posibles escenarios en los cuales la respuesta enviada no es útil.
def respuestaCorrecta(response):

    try:

        if response == None:
            raise Exception("Ha ocurrido un problema con la respuesta del servidor MongoDB")

        if response.ok == True:
            pass
        else:
            raise Exception("Ha ocurrido un problema con la respuesta del servidor MongoDB")

        if response.reason == "OK":
            pass
        else:
            raise Exception("Ha ocurrido un problema con la respuesta del servidor MongoDB")

        if response.status_code == 200:
            pass
        else:
            raise Exception("Ha ocurrido un problema con la respuesta del servidor MongoDB")
    
    except Exception:

        return False

    return True

# Recorremos la respuesta de mongo para comprobar que cumple el modelo necesario para que el programa se ejecute correctamete
def respuestaEsModelo(listaBicis):

    try: 
        assert isinstance(listaBicis,list)
    except AssertionError:
        return False

    for bici in listaBicis:

        try:
            assert isinstance(bici, dict)
        except AssertionError:
            return False

    return True

# Comprueba que el diccionario de la bici cumple con las caracteristicas necesarias para que el programa se eejcute correctamente.
def checkBiciModelo(listaBicis):

    listaValoresCorrectos = ["_idbike","state","type","techinfo","complements","prize_euros_days","where","img"]

    for bici in listaBicis:

        try:
            listaValoresBici = list(bici.keys())
        except:
            return False

        if sorted(listaValoresCorrectos) != sorted(listaValoresBici):

            return False

        try:
            for key in bici:
                bici[key]
        except KeyError:
            return False

    return True

# Comprueba que el diccionario de los rentals cumple con las caraceristicas necesarias.
def checkRentalModelo(listaRentals):

    listaValoresCorrectos = ['_idrental', 'company_name', 'address', 'social_media', 'contact', 'bikes','promotions', 'stock',"img","icono"]

    for rental in listaRentals:

        try:
            listaValoresRental = list(rental.keys())

        except:
            return False

        if sorted(listaValoresCorrectos) != sorted(listaValoresRental):

            return False

        try:
            for key in rental:
                rental[key]
        except KeyError:
            return False

    return True