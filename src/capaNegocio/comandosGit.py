import subprocess

# En este módulo vamos a crear todos los comandos necesários para poder
# visualizar los cambios efectuados en local, en la rama "página" de github
# que será la que se conecte a github pages.

# Definimos una función que ejecuta el comando gitpull
def gitPull():

    try: # Comprobamos que el comando se puede ejecutar sin problema
        comandoPull = f"git pull origin pagina"
        subprocess.run(comandoPull)
        print("Comando git pull ejecutado correctamente.")

    except subprocess.SubprocessError: # Capturamos un error en el caso de que no se pueda ejecutar correctamente
        print("El comando git pull no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")

# Definimos una función que ejecuta el comando gitcheckout y cambia a la rama "pagina"
def gitCheckout():

    try: # Comprobamos que el comando se puede ejecutar sin problema
        comandoCheckout = f"git checkout -b pagina"
        subprocess.run(comandoCheckout)
        print("Comando git checkout ejecutado correctamente.")

    except subprocess.SubprocessError: # Capturamos un error en el caso de que no se pueda ejecutar correctamente
        print("El comando git checkout no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")

# Definimos una función que ejecuta el comando gitpush
def gitPush():

    try: # Comprobamos que el comando se puede ejecutar sin problema
        comandoPush = f"git push origin pagina"
        subprocess.run(comandoPush)
        print("Comando git push ejecutado correctamente.")

    except subprocess.SubprocessError: # Capturamos un error en el caso de que no se pueda ejecutar correctamente
        print("El comando git push no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")

# Definimos una función que ejecuta el comando gitad
def gitAd():

    try: # Comprobamos que el comando se puede ejecutar sin problema
        comandoAdd = "git add ."
        subprocess.run(comandoAdd)
        print("Comando git add ejecutado correctamente.")

    except subprocess.SubprocessError: # Capturamos un error en el caso de que no se pueda ejecutar correctamente
        print("El comando git add no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")

# Definimos una función que ejecuta el comando gitcommit 
def gitCommit():

    try: # Comprobamos que el comando se puede ejecutar sin problema
        comandoCommit = f'git commit -m "update(remote:pagina): actualizar informacion de la base de datos en gitHub Pages."'
        subprocess.run(comandoCommit)
        print("Comando git commit ejecutado correctamente.")

    except subprocess.SubprocessError: # Capturamos un error en el caso de que no se pueda ejecutar correctamente
        print("El comando git commit no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")

# Definimos una función que ejecuta el comando gitmerge
def gitMerge():

    try: # Comprobamos que el comando se puede ejecutar sin problema
        comandoMerge = f"git merge develop"
        subprocess.run(comandoMerge)
        print("Comando git merge ejecutado correctamente.")

    except subprocess.SubprocessError: # Capturamos un error en el caso de que no se pueda ejecutar correctamente
        print("El comando git merge no se ha podido ejecutar correctamente, revíselo e inténtelo de nuevo.")

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