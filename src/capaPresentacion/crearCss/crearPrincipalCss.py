from src.capaPresentacion.crearCss.cssPrincipalUtilidades import footerStylesCss, headerStylesCss, baseStylesCss, navStylesCss, indexStylesCss
from src.capaPresentacion.crearArchivos import crearArchivo

def crearFooterCss():
    crearArchivo(footerStylesCss(), ".\\docs\\cssStyles", "footer", "css")

def crearHeaderCss():
    crearArchivo(headerStylesCss(), ".\\docs\\cssStyles", "header", "css")

def crearBaseCss():
    crearArchivo(baseStylesCss(), ".\\docs\\cssStyles", "base", "css")

def crearNavCss():
    crearArchivo(navStylesCss(), ".\\docs\\cssStyles", "nav", "css")

def crearIndexCss():
    crearArchivo(indexStylesCss(), ".\\docs\\cssStyles", "index", "css")

def crearMainCss():
    crearFooterCss()
    crearHeaderCss()
    crearBaseCss()
    crearNavCss()
    crearIndexCss()