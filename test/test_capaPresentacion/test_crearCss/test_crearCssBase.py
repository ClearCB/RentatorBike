from src.capaPresentacion.crearCss.funcionCssBase import footerStylesCss, headerStylesCss, navStylesCss, baseStylesCss
from src.variables.variablesCss import footerCss, headerCss, baseCss, navCss
import pytest

# Este test comprueba que las funciones que devuelven una variable con el código css de las partes header, base, nav y footer.

# Este test comprueba que se devuelve correctamente el código de la parte footercss
@pytest.mark.test_crearFooterCss
def test_crearFooterCss():

    assert footerStylesCss() == footerCss

# Este test comprueba que se devuelve correctamente el código de la parte headercss
@pytest.mark.test_crearHeaderCss
def test_crearHeaderCss():

    assert headerStylesCss() == headerCss

# Este test comprueba que se devuelve correctamente el código de la parte navcss
@pytest.mark.test_crearNavCss
def test_crearNavCss():

    assert navStylesCss() == navCss

# Este test comprueba que se devuelve correctamente el código de la parte basecss
@pytest.mark.test_crearBaseCss
def test_crearBaseCss():

    assert baseStylesCss() == baseCss