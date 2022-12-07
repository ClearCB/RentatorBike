from src.capaNegocio.crearArchivos import crearArchivo

#Funcion que define el codigo css del archivo bicis.css
def bicisStylesCss():
   
  #Definimos el valor de la variable bicisCss con el código css
    bicisCss =  '''
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
    
    return bicisCss

#Funcion que crea el archivo bicis.css en la ruta indicada.
def crearBicisCss():
    crearArchivo(bicisStylesCss(), ".\\docs\\cssStyles", "bicis", "css")
