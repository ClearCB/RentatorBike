from src.capaPresentacion.crearCss.crearPrincipalCss import headerCss, baseCss, navCss, indexCss, footerCss
import pytest
import os

@pytest.mark.test_footerCss
def test_footerStylesCss():
    footerCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\footer.css") == True


@pytest.mark.test_headerCss
def test_headerCss():
    headerCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\header.css") == True


@pytest.mark.test_baseCss
def test_baseStylesCss():
    baseCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\base.css") == True


@pytest.mark.test_navCss
def test_navStylesCss():
    navCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\base.css") == True


@pytest.mark.test_indexCss
def test_indexStylesCss():
    indexCss()
    assert os.path.isfile("C:\\WORKSPACES\\cssStyles\\base.css") == True
    

    





