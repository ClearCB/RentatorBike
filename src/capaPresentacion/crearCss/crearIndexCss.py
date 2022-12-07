from src.capaNegocio.crearArchivos import crearArchivo

#Funcion que define el codigo Css del archivo index.html
def indexStylesCss():

     #Definimos el valor de la variable indexCss con el código css.
    indexCss = '''
body{
    background-color: rgb(225, 251, 244);
}
.contenido{
    display: flex;
    flex-flow: column wrap;
    align-items: center;
}
.contenedorinfo {
    display: flex;
    flex-direction: column;
    border: 3px solid black;
    width: 60%;
    height: 450px;
    margin-top: 40px;
}
.contenedorinfo h3 {
    font-size: 30px;
    margin-left: 30px;
    color: white;
}
.contenedorinfo p{
    font-size: 20px;
    backdrop-filter: blur(20px);
    text-shadow: 1px 1px 2px black;
    width: 90%;
    margin: 0 auto;
    color: white;
}
.contenedorinfo a{
    text-decoration: none;
}
.linkpagina{
    position: absolute;
    width: 100px;
    height: auto;
    background-color: rgb(167, 238, 167);
    padding: 10px;
    right: 0;
    bottom: 0;
    margin-right: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
}
.contenedorinfo .rutas {
    width: auto;
    height: 100%;
    background-image: url(http://imgfz.com/i/DmeYNvh.jpeg);
    background-size: cover;
    background-position: center;
    position: relative;
}
.video_background {
    margin-top: 2em;
    display: flex;
    flex-direction: column;
    width: 90%;
}
.contenedorinfo iframe{
    margin-top: 30px;
    height: 100%;
}
.contenedorinfo:last-child{
    height: 700px;
}
.contenedorinfo:last-child h3 {
    display: block;
    font-size: 30px;
    margin-left: 30px;
    color: black;
}
.volverArriba .flechaSubir{
    height: 53px;
    width: 49px;
    position: fixed;
    right: 25px;
}
/* 280px — 480px: dispositivos móviles */
@media (min-width: 280px) and (max-width: 480px) {
    .contenedorinfo {
        width: 92%;
    }
    .volverArriba .flechaSubir {
        height: 25px;
        width: 25px;
    }
}
/* 481px — 768px*/
@media (min-width: 481px) and (max-width: 768px) {
    .contenedorinfo {
        width: 92%;
    }
    .volverArriba .flechaSubir {
        height: 25px;
        width: 25px;
    }
}
/* 769px — 1024px */
@media (min-width: 769px) and (max-width: 1024px) {
    .contenedorinfo {
        width: 80%; 
    }
    .volverArriba .flechaSubir {
        height: 35px;
        width: 35px;
    }
}
/* 1025px — 1200px */
@media (min-width: 1025px) and (max-width: 1200px) {
    .contenedorinfo {
        width: 70%;
    }
    .video_background {
        width: 78%;
    }
/* > 1201px: Computadoras de escritorio, pantallas grandes */
@media (min-width: 1201px) {
    .video_background {
        width: 70%;
    }
}'''

    return indexCss


#Funcion que crea el archivo index.css en la ruta indicada.
def crearIndexCss():
    
    crearArchivo(indexStylesCss(), ".\\docs\\cssStyles", "index", "css")