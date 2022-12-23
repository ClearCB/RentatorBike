from src.capaPresentacion.crearTodo import crearTodo
from src.capaNegocio.crearDirectorios import crearRutasDocs
from src.capaNegocio.comandosGit import actualizarPages


# Este modulo se va a encargar de crear y ejecutar todas las funciones para que se 
# visualicen los cambios en la base de datos de MongoDB en la pagina web estática
# servida por gitHub Pages en link : 'https://clearcb.github.io/RentatorBike/'

def generarGitHubPages():

    crearRutasDocs()
    crearTodo()
    actualizarPages()

if __name__ == '__main__':

    generarGitHubPages()