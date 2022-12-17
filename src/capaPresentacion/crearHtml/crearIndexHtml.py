from src.capaPresentacion.crearHtml.funcionHtmlBase import crearHtmlHead, crearHeader, crearCodigoHtml
from src.capaPresentacion.variables.variablesHtml import bodyIndex, footerBase, headBase, headerBase
from src.capaNegocio.crearArchivos import crearArchivo
import os

# En este módulo vamos a crear funciones que van a crear un archivo "index.html"

indexHead = crearHtmlHead(headBase, "Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike","cssStyles/","index")
indexHeader = crearHeader(headerBase, "","second_pages/")

# Definimos una función que ejecuta la función necesaria para crear el archivo correctamente.
def crearIndexHtml():

    crearArchivo(crearCodigoHtml(indexHead,indexHeader,bodyIndex,footerBase),".\\docs","index","html")
