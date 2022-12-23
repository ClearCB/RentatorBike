from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import indexCss

#Funcion que define el codigo Css del archivo index.html
def indexStylesCss():

    return indexCss


#Funcion que crea el archivo index.css en la ruta indicada.
def crearIndexCss():
    
    crearArchivo(indexStylesCss(), ".\\docs\\cssStyles", "index", "css")