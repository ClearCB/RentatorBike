import subprocess

# En este módulo vamos a crear todos los comandos necesários para poder
# visualizar los cambios efectuados en local, en la rama "página" de github
# que será la que se conecte a github pages.

# Primero haremos una función que ejecute el commando git pull


def gitPull():

    comandoPull = f"git pull origin pagina"
    subprocess.run(comandoPull)

def gitCheckout():

    comandoCheckout = f"git checkout pagina"
    subprocess.run(comandoCheckout)

def gitPush():

    comandoPush = f"git push origin pagina"
    subprocess.run(comandoPush)

def gitAd():

    comandoAdd = "git add ."
    subprocess.run(comandoAdd)

def gitCommit():

    comandoCommit = f'git commit -m "update(remote:pagina): actualizar informacion de la base de datos en gitHub Pages."'
    subprocess.run(comandoCommit)

def gitMerge():

    comandoMerge = f"git merge develop"
    subprocess.run(comandoMerge)

def guardarCambios():

    gitAd()
    gitCommit()

def actualizarGitHubPagina():

    gitCheckout()
    gitMerge()
    gitPull()
    gitPush()

guardarCambios()
actualizarGitHubPagina()