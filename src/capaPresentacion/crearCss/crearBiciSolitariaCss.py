from src.capaNegocio.crearArchivos import crearArchivo


#Funcion que define el codigo Css del archivo biciSolitaria.css
def biciSolitariaStylesCss():
    
    #Definimos el valor de la variable biciSolitariaCss con el código css
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
    
    return biciSolitariaCss

#Funcion que crea el archivo biciSolitaria.css en la ruta indicada.
def crearBiciSolitariaCss():
    crearArchivo(biciSolitariaStylesCss(), ".\\docs\\cssStyles", "bicisolitaria", "css")

