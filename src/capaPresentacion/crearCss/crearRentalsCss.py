from src.capaNegocio.crearArchivos import crearArchivo

#Funcion que define el codigo css del archivo rentals.css
def rentalsStylesCss():

    # Definimos el valor de la variable rentalsCss con el código css
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
}'''
    
    return rentalsCss

#Funcion que crea el archivo rentals.css en la ruta indicada.
def crearRentalsCss():
    crearArchivo(rentalsStylesCss(), ".\\docs\\cssStyles", "rentals", "css")
