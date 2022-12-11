from src.capaPresentacion.crearCss.funcionCssBase import footerStylesCss, headerStylesCss, navStylesCss, baseStylesCss
import pytest

# Este test comprueba que las funciones que devuelven una variable con el código css de las partes header, base, nav y footer.

# Este test comprueba que se devuelve correctamente el código de la parte footercss
@pytest.mark.test_crearFooterCss
def test_crearFooterCss():

    footerCss = '''
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

    assert footerStylesCss() == footerCss

# Este test comprueba que se devuelve correctamente el código de la parte headercss
@pytest.mark.test_crearHeaderCss
def test_crearHeaderCss():

    headerCss = '''
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

    assert headerStylesCss() == headerCss

# Este test comprueba que se devuelve correctamente el código de la parte navcss
@pytest.mark.test_crearNavCss
def test_crearNavCss():

    navCss = '''
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

    assert navStylesCss() == navCss

# Este test comprueba que se devuelve correctamente el código de la parte basecss
@pytest.mark.test_crearBaseCss
def test_crearBaseCss():

    baseCss = '''
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

    assert baseStylesCss() == baseCss