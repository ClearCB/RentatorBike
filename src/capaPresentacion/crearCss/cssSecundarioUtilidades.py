def bicisStylesCss():
    return  '''#contenedorPadre {
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
}
'''

def biciSolitariaStylesCss():
    return  '''.titleBicis{
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
}
'''

def marcasStylesCss():
    return  '''
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
}
'''

def rentalsStylesCss():
    return  '''.rentals {
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
/* 280px — 480px: dispositivos móviles */
@media (min-width: 280px) and (max-width: 480px) {
   .rentals__container {
    flex-direction: column;
    row-gap: 15px;
}
}
/* 481px — 768px*/
@media (min-width: 481px) and (max-width: 768px) {
    .rentals__container {
    flex-direction: column;
    row-gap: 15px;
}
}
'''



def bicisfiltroStylesCss():
    return  '''#contenedorPadre {
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
 /* INICIO 320px — 560px: estilos para los botones de navegacion bicis característica  */
@media (min-width: 320px) and (max-width: 560px) {
    .categorias {
          display: flex;
          justify-content: space-around;
          flex-direction: column;
          width: 195px;
          margin: 0 auto;
    }
}
/* FIN  320px — 560px: estilos para los botones de navegacion bicis característica  */
'''
