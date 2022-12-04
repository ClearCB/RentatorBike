import subprocess

# En este módulo vamos a crear todos los comandos necesários para poder
# visualizar los cambios efectuados en local, en la rama "página" de github
# que será la que se conecte a github pages.

# Primero haremos una función que ejecute el commando git pull


def gitPull(ramaRemotoObjetivo):

    comandoPull = f"git pull origin {ramaRemotoObjetivo}"
    subprocess.run(comandoPull)

def gitCheckout(ramaLocalObjetivo):

    comandoCheckout = f"git checkout  {ramaLocalObjetivo}"
    subprocess.run(comandoCheckout)

def gitPush(ramaLocalObjetivo):

    comandoPush = f"git push origin  {ramaLocalObjetivo}"
    subprocess.run(comandoPush)

def gitAd():

    comandoAdd = "git add ."
    subprocess.run(comandoAdd)

def gitCommit(ramaLocalObjetivo):

    comandoCommit = f'git commit -m "update({ramaLocalObjetivo}): actualizar informacion de la base de datos en gitHub Pages."'
    subprocess.run(comandoCommit)

def gitMerge(ramaLocal):

    comandoMerge = f"git merge {ramaLocal}"
    subprocess.run(comandoMerge)

def guardarCambios():

    gitAd()
    gitCommit("comandosGit")

def actualizarGitHubPagina(ramaLocal, ramaLocalObjetivo, ramaRemotoObjetivo):

    gitCheckout(ramaLocalObjetivo)
    gitMerge(ramaLocal)
    gitPull(ramaRemotoObjetivo)
    gitPush(ramaLocalObjetivo)

guardarCambios()
actualizarGitHubPagina("comandosGit","develop","develop")
