from selenium.webdriver.common.by import By
from UTILS.driver_factory import crear_driver


def test_login_exitoso_saucedemo():
    """Valida que un usuario pueda iniciar sesión correctamente en Sauce Demo."""

    driver = crear_driver()

    try:
        # 1. Navego a la página de login
        driver.get("https://www.saucedemo.com")

        # 2. Ingreso credenciales válidas
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # 3. Click en el botón de login
        driver.find_element(By.ID, "login-button").click()

        # 4. Valido login exitoso
        assert "/inventory.html" in driver.current_url

    finally:
        driver.quit()