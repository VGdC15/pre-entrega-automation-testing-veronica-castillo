from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_exitoso_saucedemo(driver, credenciales_validas):
    """Valida que un usuario pueda iniciar sesión correctamente en Sauce Demo."""
    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url