from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader
from src.capaPresentacion.variables.variablesHtml import bodyIndex, footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo
import os

# En este módulo vamos a crear funciones que van a crear un archivo "index.html"

# Función que construye el index.html pasandole los parámetros correctos y lo devuelve en una variable
def indexHtml(head, header, body, footer):

    index = ''''''

    # Añadimos cada parte del código independientemente 
    index += head
    index += header
    index += body
    index += footer

    return index # Devolvemos la variable index que contiene el código del archivo index.html


    index = ''''''
    # Añadimos cada parte del código independientemente 
    index += crearHtmlHead(head, "Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike","cssStyles/","index")
    index += crearHeader(header, "","second_pages/")
    index += bodyIndex
    index += footer

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearIndexHtml():

    crearArchivo(indexHtml(),".\\docs","index","html")
