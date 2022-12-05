from capaPresentacion.crearCss.cssPrincipalBase import footerStylesCss, headerStylesCss, baseStylesCss, navStylesCss, indexStylesCss

def footerCss():
    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles\\footer.css","w", encoding="utf-8") as archivo:
         archivo.write(footerStylesCss())
    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")


def headerCss():
    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles\\header.css","w", encoding="utf-8") as archivo:
         archivo.write(headerStylesCss())
    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

def baseCss():
    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles\\base.css","w", encoding="utf-8") as archivo:
         archivo.write(baseStylesCss())
    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

def navCss():
    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles\\nav.css","w", encoding="utf-8") as archivo:
         archivo.write(navStylesCss())
    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

def indexCss():
    try:
        with open("C:\\Users\\abelc\\Desktop\\github\\RentatorBike\\docs\\cssStyles\\index.css","w", encoding="utf-8") as archivo:
         archivo.write(indexStylesCss())
    except FileNotFoundError:
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")

def mainCss():
    footerCss()
    headerCss()
    baseCss()
    navCss()
    indexCss()