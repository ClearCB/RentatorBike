from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesHtml import htmlBiciSolitaria
from src.capaPresentacion.crearHtml.funcionHtmlBase import biciSolitariaHtml
from src.capaDatos.listarDatosMongo import listarBicis, respuestaText
from src.capaDatos.peticionMongo import respuestaMongo

# Definimos la lista de las bicis que le pasaremos a la funcion que crea cada html en solitario de cada bici
listaBicis = listarBicis(respuestaText(respuestaMongo())) 

# Definimos una función que ejecuta la función necesaria para crear los archivos bicissolitarias correctamente.
def crearBiciSolitariaHtml(lista):

    for bici in lista: # Recorremos la lista de las bicis

        id = bici["_idbike"]
        bicisolitaria = biciSolitariaHtml(htmlBiciSolitaria, bici) # Creamos un html con los datos de la bici en concreto
        crearArchivo(bicisolitaria,".\\docs\\second_pages\\bicissolitarias\\",f"bicissolitaria{id}","html")