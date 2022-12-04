import subprocess

# En este módulo vamos a crear todos los comandos necesários para poder
# visualizar los cambios efectuados en local, en la rama "página" de github
# que será la que se conecte a github pages.

# Primero haremos una función que ejecute el commando git pull


def gitPull():

    comandoPull = "git pull origin pagina"
    subprocess.run(comandoPull)

gitPull()
