from src.capaNegocio.crearArchivos import crearArchivo

#Funcion que define el codigo Css del archivo footer.css
def footerStylesCss():
  
     #Definimos el valor de la variable css con el código css
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
}
.soporte_links ul {
  padding-left: 0px;
}
.soporte_links ul, li{
  list-style: none;
}
.soporte_links a{
  text-decoration: none;
}'''
   
    return footerCss


#Funcion que define el codigo css del archivo header.css
def headerStylesCss():

     #Definimos el valor de la variable headerCss con el código css
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

    return headerCss


#Funcion que define el codigo css del archivo base.css
def baseStylesCss():
    
     #Definimos el valor de la variable base con el código css
    baseCss =  '''
body {
     margin: 0;
     background-color:rgb(255, 255, 255);
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

    return baseCss


#Funcion que define el codigo css del archivo nav.css
def navStylesCss():
    
    #Definimos el valor de la variable nav con el código css
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

@media only screen and (min-width: 350px) 
    and (max-width:800px) 
    and (orientation: portrait) {

    #nav{
        display: flex;
        width: auto;
        justify-content: space-between;
        margin: 0px 0px 0px 0px;
    }

    #nav ul li{
        font-size: 10px;
    }
}'''

    return navCss



def crearCssBase():

    #Funcion que crea el archivo footer.css en la ruta indicada.
    crearArchivo(footerStylesCss(), ".\\docs\\cssStyles", "footer", "css")

    #Funcion que crea el archivo header.css en la ruta indicada.
    crearArchivo(headerStylesCss(), ".\\docs\\cssStyles", "header", "css")

    #Funcion que crea el archivo base.css en la ruta indicada.
    crearArchivo(baseStylesCss(), ".\\docs\\cssStyles", "base", "css")

    #Funcion que crea el archivo nav.css en la ruta indicada.
    crearArchivo(navStylesCss(), ".\\docs\\cssStyles", "nav", "css")

