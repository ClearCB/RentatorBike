# Vamos a realizar los test de las funcionalidades del modulo htmlBase para comprobar
# que se comportan como queremos

from src.capaPresentacion.funcionHtmlBase import crearHtmlHead
import pytest

# En primer lugar, un test que nos permite comprobar que los parametros asignados se introducen en la variable.

@pytest.mark.test_crearHtmlHead
def test_crearHtmlHead():

    
    head = f'''
<!DOCTYPE html>
<!-- Hemos añadido el atributo lang en la etiqueta html en lugar de hacerlo en meta porque el validador nos daba problemas -->
<html lang="es" dir="ltr">
    <head>
        <!-- La etiqueta meta la hemos obviado ya que en el footer hemos incluido una licencia de Creative Commons, sin embargo esta sería su sintaxis:  
        <meta name="copyright" content="Licencia de la empresa RentatorSL, propiedad de Gema Marquinez y Abel Casas"-->
        <title>Rentator</title>
        <base target="_blank">
        <meta charset="UTF-8">
        <meta name="author" content="Gema Marquinez y Abel Casas">
        <meta name="description" content="Página principal de un buscador de bicicletas para alquilar">
        <meta name="generator" content="Visual Studio Code">
        <meta name="keywords" content="Bicicletas, inicio, index, alquilar, rental, bike">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="cssStyles/footer.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/header.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/base.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/nav.css">
        <link rel="stylesheet" type="text/css" href="cssStyles/index.css">
    </head>
'''
    
    assert crearHtmlHead("Rentator", "Página principal de un buscador de bicicletas para alquilar", "Bicicletas, inicio, index, alquilar, rental, bike", "cssStyles/", 'index') == head
