import subprocess

# En este módulo vamos a crear todos los comandos necesários para poder
# visualizar los cambios efectuados en local, en la rama "página" de github
# que será la que se conecte a github pages.

# Definimos una función que ejecuta el comando gitpull
def comandoGit(comando):

    try:
        comand = subprocess.run(comando, shell=True)
        if comand.returncode != 0 and comand.returncode != 1:
            raise Exception
        else:
            print(f"El comando {comando} se ha ejecutado correctamente")
            return True
    except:
        print(f"El comando {comando} no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")
        return False

# Definimos una función que ejecuta el comando gitad
def gitAd():

    comandoGit("git add .")

# Definimos una función que ejecuta el comando gitcommit 
def gitCommit():

    comandoGit("git commit -m 'Actualizar'")

def gitPull():

    comandoGit("git pull origin main")

# Definimos una función que ejecuta el comando gitpush
def gitPush():

    comandoGit("git push origin main")
    print("Los cambios han sido actualizado para visitar la pagina web visite el siguiente link:'LINK'")

# Definimos una función que ejecuta los comandos gitad y git commit para guardar los cambios
def guardarCambios():

    gitAd()
    gitCommit()

# Definimos una función que ejecuta los comandos gitcheckout gitmerge gitpull y gitpush para actualizar la pagina en el remoto
def actualizarGitHubPagina():

    gitPull()
    gitPush()

def actualizarPages():

    guardarCambios()
    actualizarGitHubPagina()