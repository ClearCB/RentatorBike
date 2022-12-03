# En este modulo vamos a definir todas las funcionalidades que van a definir y 
# estan relacionadas con la estructura común de nuestros html: "head", "header", "footer" y "nav"
# que serán llamadas desde otro modulo para printar el contenido en un archivo ".html"


# La primera función, a raiz de una serie de parámetros, va a devolver la función head

def crearHtmlHead(titulo, descripcion, keywords, cssPath, cssLink):

    head = f'''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>{titulo}</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="{descripcion}">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="{keywords}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="{cssPath}footer.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}header.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}base.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}nav.css">
        <link rel="stylesheet" type="text/css" href="{cssPath}{cssLink}.css">
    </head>
'''
    
    return head