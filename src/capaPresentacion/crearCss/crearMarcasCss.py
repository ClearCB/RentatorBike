from src.capaNegocio.crearArchivos import crearArchivo

#Funcion que define el codigo css del archivo marcas.css

def marcasStylesCss():

     #Definimos el valor de la variable marcas con el código css
    marcas =  '''
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

    return marcas

#Funcion que crea el archivo marcas.css en la ruta indicada.
def crearMarcasCss():

    crearArchivo(marcasStylesCss(), ".\\docs\\cssStyles", "marcas", "css")
