from src.capaNegocio.crearArchivos import crearArchivo

#Funcion que define el codigo Css del archivo tipos.css

def tiposStylesCss():

    # Definimos el valor de la variable footerCss con el código css
    tipos =  '''
.contenedor{
  display: flex;
  align-items: center;
}
.tiposbici_container{
    display: flex;
    flex-direction: column;
    width: 80%;
}
#tiposbici {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.flex-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
#tiposbici h4 {
  font-size: 25px;
}
.redirectionButton {
    display: inline-block;
    padding: 0px 32px 0px 32px;
    height: 48px;
    box-shadow: 0px 2px 0px #00BB31;
    background-color: #8EDD65;
    color: white; 
  }
.buttonBike{
    display: flex;
 flex-direction: row-reverse;
 margin-left: 20px;
}
button:hover {
    background-position: center;
    background: #00BB31 radial-gradient(circle, transparent 1%, #00BB31 1%) center/15000%;
  }
.flex-item {
    width: 49%;
    border-radius: 3px;
    border: solid 2px;
    text-align: center;
  }
.flex-item-description {
    width: 100%;
    text-align: center;
  }
.titleBicis{
    text-align:center;
    font-size: 50px;
    color: rgb(56, 146, 46);
  }
  /* 280px — 480px:*/
@media (min-width: 280px) and (max-width: 480px) {
  .flex-container {
    flex-direction: column;
  }
.flex-item {
    width: 100%;
  }
}
/* 481px — 768px*/
@media (min-width: 481px) and (max-width: 768px) {
  .flex-container {
    flex-direction: column;
  }
.flex-item {
    width: 100%;
  }
}'''

    return tipos


    #Funcion que crea el archivo crearTipos.css en la ruta indicada.
def crearTiposCss():
    crearArchivo(tiposStylesCss(), ".\\docs\\cssStyles", "tipos", "css")
