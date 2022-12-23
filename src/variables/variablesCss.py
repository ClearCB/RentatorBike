# Vamos a definir todas las variables de los css que utilizaran las funciones

# crearBicisCss
bicisCss =    '''
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

# crearBicisSolitariasCss
biciSolitariaCss =  '''
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

# crearBicisFiltro
bicisFiltroCss = '''
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

# crearIndexCss
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
    border: 3px solid black;
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

# crearMarcasCss
marcasCss =  '''
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

# crearRentalsCss
rentalsCss =  '''
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

# crearFooterCss
footerCss =  '''
footer {
  display: flex;
  background-color: grey;
  position: relative;
  bottom: 0;
  width: 100%;
  height: auto;
  color: rgb(0, 0, 0);
  justify-content: space-evenly;
  margin-top: 20px;
  z-index: 0;
}
.copyright_footer a{
  text-decoration: none;
  color:white;
}
.soporte_links ul {
  padding-left: 0px;
}
.soporte_links ul, li{
  list-style: none;
}
.soporte_links a{
  text-decoration: none;
  color:white;
}

/* Inicio de media-queries para dispositivo "Samsung Galaxy S8+" en modo vertical:  píxeles 360x740 */
@media (min-width: 360px) and (max-width: 740px){
footer {
  flex-direction: column-reverse;
  align-items: center;
  align-content: center;
}

.soporte_links {
  width: 100%;
}

.soporte_links ul, .footer__license__description, .footer__license__img {
  margin: 15px;
}

.copyright_footer {
  width: 100%;
}
}'''

# crearHeaderCss
headerCss =  '''
.header {
  background: #edeebc;
  overflow: hidden;
  position: relative;
}
.header__logo {
  height: 150px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-direction: column;
  position: relative;
  left: 20%;
}
.header__logo h1,
.header__logo h2 {
  font-family: "Century Gothic";
  font-weight: normal;
  margin: 0;
  text-transform: uppercase;
}
.header__logo h1 {
  font-size: 3.6rem;
  margin-bottom: 5px;
}
.header__logo h2 {
  font-size: 1.7rem;
}
.header__nav {
  position: absolute;
  z-index: 2;
  top: 0;
  right: -350px;
  transition: right 0.3s ease;
  background: #ff9200;
  clip-path: polygon(0px 0px, 35% 100%, 100% 100%, 100% 0%, 75% 0px);
}
.header:hover .header__nav {
  right: 0;
}
.header__links {
  position: relative;
  display: flex;
  flex-direction: column;
  top: 33px;
  width: 500px;
  height: 500px;
  left: 150px;
  z-index: 3;
}
.header__links a {
  color: #000;
  cursor: pointer;
  display: inline-block;
  font-family: arial;
  font-size: 1.2rem;
  font-weight: bold;
  margin: 15px 60px 0 -200px;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
}


/* Inicio de media-queries para dispositivo "Samsung Galaxy S8+" en modo vertical:  píxeles 360x740 */

@media only screen and (min-width: 350px) 
    and (max-width:800px) 
    and (orientation: portrait) {

    header {
        background: #edeebc;
        overflow: hidden;
        position: relative;
      }
    .header {
        display: block;
        position: relative;
        left: -10%;
    }

    .header__nav {
        display: none;
    }
    .header__logo {
        display: flex;
        padding-right: 100px;
    }    
    
}'''

# crearBaseCss
baseCss =  '''
body {
     margin: 0;
     background-color:rgb(225, 251, 244);
}
#search {
    border: 2px solid;
    border-radius: 15px;
    font-size: 16px;
    height: 45px;
    outline: none;
    padding: 0 8px;
    width: 50%;
}
form{
    text-align: center;
    margin-bottom: 2em;
    margin-top: 2rem;
}'''

# crearNavCss
navCss =  '''
#nav {
    display: block;
    background: #54aa51;
    width: 100%;
    position: relative;
  }
#nav ul {
    list-style: none;
    overflow: hidden;
    margin: 0;
  }
#nav ul li {
    float: left;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
  }
#nav ul li a {
    display: block;
    padding: 20px;
    color: #fff;
    text-decoration: none;
  }
#nav ul li a:hover {
    background: #f0b967;
  }
.bicisfiltroboton{
    display: block;
    padding: 20px;
    color: #fff;
    text-decoration: none;
  }
.bicisfiltroboton ul{ 
    
    display:none;
    position:absolute;
    top:100%;
    left:0;
    background:#54aa51;
    padding:0;
   }
.bicisfiltroboton:hover > ul{ 
    display: flex;
    flex-direction: column;
    position:absolute;
    left: 7%;
  }
.volverArriba .flechaSubir{
    height: 53px;
    width: 49px;
    position: fixed;
    right: 25px;
    bottom: 20%;
}

/* Inicio de media-queries para dispositivo "Samsung Galaxy S8+" en modo vertical:  píxeles 360x740 */
@media (min-width: 360px) and (max-width: 740px) {

#nav{
    display: flex;
    width: auto;
    justify-content: space-between;
    margin: 0px 0px 0px 0px;
}

#nav ul li{
        font-size: 12px;
}
}'''