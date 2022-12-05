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

def headerStylesCss():
    return  '''.header {
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
  font-size: 2.5rem;
  margin-bottom: 5px;
}
.header__logo h2 {
  font-size: 1.5rem;
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
  font-size: 1rem;
  font-weight: bold;
  margin: 15px 60px 0 -200px;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
}
/* 320px — 480px: dispositivos móviles */
@media (min-width: 320px) and (max-width: 480px) {
}
/* 481px — 768px */
@media (min-width: 481px) and (max-width: 768px) {
}
/* 769px — 1024px */
@media (min-width: 769px) and (max-width: 1024px) {
}
/* 1025px — 1200px*/
@media (min-width: 1025px) and (max-width: 1200px) {
}
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

def navStylesCss():
    return  '''#nav {
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


def indexStylesCss():
    return  '''body{
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
/* 280px — 480px: dispositivos móviles */
@media (min-width: 280px) and (max-width: 480px) {
    .contenedorinfo {
        width: 92%;
    }
    .volverArriba .flechaSubir {
        height: 25px;
        width: 25px;
    }
}
/* 481px — 768px*/
@media (min-width: 481px) and (max-width: 768px) {
    .contenedorinfo {
        width: 92%;
    }
    .volverArriba .flechaSubir {
        height: 25px;
        width: 25px;
    }
}
/* 769px — 1024px */
@media (min-width: 769px) and (max-width: 1024px) {
    .contenedorinfo {
        width: 80%; 
    }
    .volverArriba .flechaSubir {
        height: 35px;
        width: 35px;
    }
}
/* 1025px — 1200px */
@media (min-width: 1025px) and (max-width: 1200px) {
    .contenedorinfo {
        width: 70%;
    }
    .video_background {
        width: 78%;
    }
/* > 1201px: Computadoras de escritorio, pantallas grandes */
@media (min-width: 1201px) {
    .video_background {
        width: 70%;
    }
}
'''