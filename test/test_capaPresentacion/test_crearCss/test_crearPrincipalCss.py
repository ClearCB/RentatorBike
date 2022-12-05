from src.capaPresentacion.crearCss.crearPrincipalCss import crearHeaderCss, crearBaseCss, crearNavCss, crearIndexCss, crearFooterCss
import pytest
import os

@pytest.mark.test_crearFooterCss
def test_crearFooterCss():
    crearFooterCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\footer.css") == True


@pytest.mark.test_crearHeaderCss
def test_crearHeaderCss():
    crearHeaderCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\header.css") == True


@pytest.mark.test_crearBaseCss
def test_crearBaseCss():
    crearBaseCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\base.css") == True


@pytest.mark.test_crearNavCss
def test_crearNavCss():
    crearNavCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\nav.css") == True


@pytest.mark.test_crearIndexCss
def test_crearIndexCss():
    crearIndexCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\index.css") == True
    

    





