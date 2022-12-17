# En este modulo vamos a definir todas las funcionalidades que van a definir y 
# estan relacionadas con la estructura común de nuestros html: "head", "header", "footer" y "nav"
# que serán llamadas desde otro modulo para printar el contenido en un archivo ".html"

# Esta función a raiz de una serie de parámetros, va a devolver la variable head que contiene el código html de la parte head.
def crearHtmlHead(head, titulo, descripcion, keywords, cssPath, cssLink):

    head=head.replace("-titulo-", titulo)
    head=head.replace("-descripcion-", descripcion)
    head=head.replace("-keywords-",keywords)
    head=head.replace("-csspath-",cssPath)
    head=head.replace("-csslink-",cssLink)
    
    return head

# Esta funcion a raiz de una serie de parámetros, va a devolver la variable header que contiene el código html de la parte del header/nav
def crearHeader(header, indexPath, path):

    header=header.replace("-indexpath-",indexPath)
    header=header.replace("-path-",path)

    return header
