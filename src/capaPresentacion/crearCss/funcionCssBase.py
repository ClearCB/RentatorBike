from src.capaNegocio.crearArchivos import crearArchivo
from src.variables.variablesCss import footerCss, headerCss, baseCss, navCss

#Funcion que define el codigo Css del archivo footer.css
def footerStylesCss():
   
    return footerCss


#Funcion que define el codigo css del archivo header.css
def headerStylesCss():

    return headerCss


#Funcion que define el codigo css del archivo base.css
def baseStylesCss():
    
    return baseCss


#Funcion que define el codigo css del archivo nav.css
def navStylesCss():

    return navCss



def crearCssBase():

    #Funcion que crea el archivo footer.css en la ruta indicada.
    crearArchivo(footerStylesCss(), ".\\docs\\cssStyles", "footer", "css")

    #Funcion que crea el archivo header.css en la ruta indicada.
    crearArchivo(headerStylesCss(), ".\\docs\\cssStyles", "header", "css")

    #Funcion que crea el archivo base.css en la ruta indicada.
    crearArchivo(baseStylesCss(), ".\\docs\\cssStyles", "base", "css")

    #Funcion que crea el archivo nav.css en la ruta indicada.
    crearArchivo(navStylesCss(), ".\\docs\\cssStyles", "nav", "css")

