from src.capaNegocio.comandosGit import comandoGit, actualizarPages, gitAd, gitCommit, gitPull, gitPush, guardarCambios, actualizarGitHubPagina

def test_comandoGit():

    assert comandoGit("dir") == True

def test_comandosGitError():

    assert comandoGit("ls") == False

def test_comandoGitAd():

    assert gitAd() == True

def test_comandoGitCommit():

    assert gitCommit() == True

def test_comandoGitPull():

    assert gitPull() == True

def test_comandoGitPush():

    assert gitPush() == True

def test_guardarCambios():

    assert guardarCambios() == True

def test_actualizarGitHub():

    assert actualizarGitHubPagina() == True

def test_actualizarPages():

    assert actualizarPages() == True