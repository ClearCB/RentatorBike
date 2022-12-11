from src.capaPresentacion.crearCss.crearBicisCss import bicisStylesCss
from src.capaPresentacion.crearCss.crearBicisFiltroCss import bicisfiltroStylesCss
from src.capaPresentacion.crearCss.crearBiciSolitariaCss import biciSolitariaStylesCss
from src.capaPresentacion.crearCss.crearIndexCss import indexStylesCss
from src.capaPresentacion.crearCss.crearMarcasCss import marcasStylesCss
from src.capaPresentacion.crearCss.crearRentalsCss import rentalsStylesCss
import pytest

# Este test comprobará que las funcionalidades que crean el css de las paginas en solitario lo hacen correctamente

# Este test comprueba que se crea correctamente el codigo css de la pagina bicis.html
@pytest.mark.test_crearBicisCss
def test_crearBicisCss():

    bicisCss = '''
#contenedorPadre {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  column-gap: 0%;
  width: 95%;
  margin: 0 auto;
  margin-top: 2em;
}
.container {
  width: 300px;
  height: auto;
  margin: 1%;
  border: 0px solid rgb(0, 0, 0);
  border-radius: 8px;
  box-shadow: green 0px 2px 5px 0px;
  flex-direction: column;
  display: flex;
  background-color: white;
  padding: 10px;
}
.infoBike {
  background-color: rgba(174, 244, 94, 0.686);
  margin: auto;
  padding-top: 2px;
  padding-bottom: 2px;
  border-radius: 10px; 
}
h2, h5 {
  text-align: center;
}
.img,
.img img {
  width: 100%;
}
.img :hover {
  transform: scale(1.10);
}
.titleBicis{
  text-align:center;
  font-size: 50px;
  color: rgb(56, 146, 46);
}
.ubicationShow{
  text-align: center;
  margin-bottom: 20px;
}'''
    assert bicisStylesCss() == bicisCss

# Este test comprueba que se crea correctamente el codigo css de la pagina por filtro css
@pytest.mark.test_crearBiciFiltroCss
def test_crearBiciFiltroCss():

    biciFiltroCss = '''
#contenedorPadre {
     display: flex;
     justify-content: center;
     align-items: center;
     flex-wrap: wrap;
     column-gap: 0%;
     width: 95%;
     margin: 0 auto;
     margin-top: 2em;
}
.container {
     width: 300px;
     height: auto;
     margin: 1%;
     border: 0px solid rgb(0, 0, 0);
     border-radius: 8px;
     box-shadow: green 0px 2px 5px 0px;
     flex-direction: column;
     display: flex;
     background-color: white;
     padding: 10px;
}
.infoBike {
     background-color: rgba(174, 244, 94, 0.686);
     margin: auto;
     padding-top: 2px;
     padding-bottom: 2px;
     border-radius: 10px;
}
 h2, h5 {
     text-align: center;
}
 .img, .img img {
     width: 100%;
}
.img :hover {
     transform: scale(1.10);
}
.titleBicis{
     text-align:center;
     font-size: 50px;
     color: rgb(56, 146, 46);
     margin-bottom: 20px;
}
.categorias{
     display: flex;
     justify-content: space-around;
}
.categorias a{
     text-decoration: none;
}
.nombrecategorias{
     background-color: rgb(122, 206, 127);
    color: white;
    border: 1px solid black;
    border-radius: 15px;
    padding: 5px;
    height: 40px;
    margin-top: 10px;
    margin-bottom: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.nombrecategorias:hover{
     background-color: green;
}
.filtrotitulo {
     font-size: 30px;
     width: 100%;
     margin-left: 8%;
     color: rgb(10, 63, 10);
}
.filtrocaract {
     font-size: 20px;
     width: 100%;
     color: rgb(4, 31, 14);
     text-align:center;
}

/* Inicio de media-queries para dispositivo "Samsung Galaxy S8+" en modo vertical:  píxeles 360x740 */
@media (min-width: 360px) and (max-width: 740px) {
.categorias {
     display: flex;
     justify-content: space-around;
     flex-direction: column;
     width: 195px;
     margin: 0 auto;
}
.container {
margin-bottom: 5%;
}
}'''

    assert bicisfiltroStylesCss() == biciFiltroCss

# Este test comprueba que se crea correctamente el codigo css de la pagina bicisolitaria.html
@pytest.mark.test_crearBiciSolitariaCss
def test_crearBiciSolitariaCss():

    biciSolitariaCss = '''
.titleBicis{
    text-align:center;
    font-size: 50px;
    color: rgb(56, 146, 46);
  }
.biciinformacion {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
}
.descripcion {
    font-size: 20px;
    margin: 20px;
}
.img{
    border: 2px solid;
    border-image: linear-gradient(90deg, rgb(0, 0, 0), rgb(255, 0, 0)) 1;
    margin-top: 50px;
    margin-bottom: 50px;
}
table{
    margin-bottom: 15px;
}
th {
    align-content: center;
    padding: 10px 10px 10px 10px;
    background-color: rgb(112, 196, 105);
    font-weight: normal;
    text-align: center;
    color: rgb(255, 255, 255);
}
td {
    align-content: center; 
    padding: 10px 10px 10px 10px;
    background-color: rgb(238, 238, 238);
}'''
    assert biciSolitariaStylesCss() == biciSolitariaCss

# Este test comprueba que se crea correctamente el codigo css de la pagina index.html
@pytest.mark.test_crearIndexCss
def test_crearIndexCss():

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
/* Inicio de media-queries para dispositivo "Samsung Galaxy S8+" en modo vertical:  píxeles 360x740 */
@media (min-width: 360px) and (max-width: 740px) {
.contenedorinfo {
     width: 92%;
    }
.volverArriba .flechaSubir {
    height: 25px;
    width: 25px;
    }
}'''
    assert indexStylesCss() == indexCss

# Este test comprueba que se crea correctamente el codigo css de la pagina marcas.html
@pytest.mark.test_crearMarcasCss
def test_crearMarcasCss():

    marcasCss = '''
#container{
  position: relative;
  text-align: center;
}
.box{
  width: 300px;
  height: 200px;
  border:2px solid green;
  margin: .5em;
  text-align:center;
  line-height: 200px;
  font-size:2.5em;
  display: inline-block;
  font-weight:bold;
  font-family :times new roman;
  margin-top: 50px;
  margin-bottom: 60px;
}
#container a{
  color: rgb(0, 0, 0);
}
.titleBike{
  text-align:center;
  font-size: 50px;
  color: rgb(56, 146, 46);
}'''
    assert marcasStylesCss() == marcasCss

# Este test comprueba que se crea correctamente el codigo css de la pagina rentals.html
@pytest.mark.test_crearRentalsCss
def test_crearRentalsCss():

    rentalsCss = '''
.rentals {
    display: flex;
    justify-content: center;
}
.rentals__container {
        display: flex;
    width: 80%;
    justify-content: space-between;
    border: 1px solid green;
    padding: 15px;
    margin-bottom:30px;
}
.rentals__titulo__logo {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-basis: 33%;
}
.rentals__description {
    display: flex;
    justify-content: center;
    flex-basis: 33%;
}
.rentals__description ul {
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    width: 90%;
    row-gap: 16px;
    margin-top: 10px;
}
.rentals__img__location {
    flex-basis: 33%;
}
.titleRental{
    text-align:center;
    font-size: 50px;
    color: rgb(56, 146, 46);
  }
.fotoRental {
    width:400px;
    height: 200px;
}
.rentalIcono {
    width:100px;
    height:100px;
    display: flex;
}

/* Inicio de media-queries para dispositivo "Samsung Galaxy S8+" en modo vertical:  píxeles 360x740 */
@media (min-width: 360px) and (max-width: 740px) {
  
.rentals__container {
    flex-direction: column;
    row-gap: 15px;
}
.fotoRental {
    display: flex;
    width: 100%;
}
}'''
    assert rentalsStylesCss() == rentalsCss