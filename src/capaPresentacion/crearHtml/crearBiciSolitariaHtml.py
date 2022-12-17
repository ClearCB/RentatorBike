from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesHtml import htmlBiciSolitaria
from src.capaPresentacion.crearHtml.funcionHtmlBase import biciSolitariaHtml

# Definimos una función que ejecuta la función necesaria para crear los archivos bicissolitarias correctamente.
def crearBiciSolitariaHtml(listaBicis):

    for bici in listaBicis: # Recorremos la lista de las bicis

        id = bici["_idbike"]
        bicisolitaria = biciSolitariaHtml(htmlBiciSolitaria, bici) # Creamos un html con los datos de la bici en concreto 
        crearArchivo(bicisolitaria,".\\docs\\second_pages\\bicissolitarias\\",f"bicissolitaria{id}","html")


