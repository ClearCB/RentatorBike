def footerStylesCss():
    return  '''footer {
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
/* 280px — 480px */
@media (min-width: 280px) and (max-width: 480px) {
}
/* 481px — 768px */
@media (min-width: 481px) and (max-width: 768px) {
}
/* 769px — 1024px*/
@media (min-width: 769px) and (max-width: 1024px) {
}
/* 1025px — 1200px */
@media (min-width: 1025px) and (max-width: 1200px) {
}
/* INICIO ESTILOS PARA dispositivos móviles, iPads, tabletas, iPads, tabletas */
@media (min-width: 280px) and (max-width:1024px)  { 
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
}
/* FIN ESTILOS PARA dispositivos móviles, iPads, tabletas, iPads, tabletas */
'''



def baseStylesCss():
    return  '''body {
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
}
/* INICIO ESTILOS HASTA 480px */
@media (max-width:1080px)  { 
    .video_background video {
        margin: 0 auto;
        width: 90%;
    }
}
/* FIN ESTILOS HASTA 480px */
'''

# Esta función define el valor del código del nav de nuestra pagina.
def navStylesCss():
    
    # Definimos el valor de la variable navCss con el código css.
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
  .volverarriba {
    position: fixed;
    left: 80%;
    padding: 0px 32px 0px 32px;
    top: 90%;
    height: 48px;
    background-color: #8EDD65;
    color: white;
    z-index: 1;
  }
.volverarriba:hover {
    background-position: center;
    background: #00BB31 radial-gradient(circle, transparent 1%, #00BB31 1%) center/15000%;
    z-index: 1;
  }
'''

    return navCss