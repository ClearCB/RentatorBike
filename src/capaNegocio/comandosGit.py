import subprocess

# En este módulo vamos a crear todos los comandos necesários para poder
# visualizar los cambios efectuados en local, en la rama "página" de github
# que será la que se conecte a github pages.

# Definimos una función que ejecuta el comando gitpull
def gitPull():

    comandoPull = f"git pull origin pagina"
    subprocess.run(comandoPull)

# Definimos una función que ejecuta el comando gitcheckout
def gitCheckout():

    comandoCheckout = f"git checkout pagina"
    subprocess.run(comandoCheckout)

# Definimos una función que ejecuta el comando gitpush
def gitPush():

    comandoPush = f"git push origin pagina"
    subprocess.run(comandoPush)

# Definimos una función que ejecuta el comando gitad
def gitAd():

    comandoAdd = "git add ."
    subprocess.run(comandoAdd)

# Definimos una función que ejecuta el comando gitcommit 
def gitCommit():

    comandoCommit = f'git commit -m "update(remote:pagina): actualizar informacion de la base de datos en gitHub Pages."'
    subprocess.run(comandoCommit)

# Definimos una función que ejecuta el comando gitmerge
def gitMerge():

    comandoMerge = f"git merge develop"
    subprocess.run(comandoMerge)

# Definimos una función que ejecuta los comandos gitad y git commit para guardar los cambios
def guardarCambios():

    gitAd()
    gitCommit()

# Definimos una función que ejecuta los comandos gitcheckout gitmerge gitpull y gitpush para actualizar la pagina en el remoto
def actualizarGitHubPagina():

    gitCheckout()
    gitMerge()
    gitPull()
    gitPush()