import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import obtener_datos_prueba


DATOS_LOGIN_INVALIDO = obtener_datos_prueba()["usuarios"]["invalidos"]


@pytest.mark.login
def test_login_exitoso_saucedemo(driver, credenciales_validas):
    """Valida que un usuario pueda iniciar sesión correctamente en Sauce Demo."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"],
    )

    inventory_page = InventoryPage(driver).esperar_carga()

    assert inventory_page.esta_en_pagina_inventario()
    assert inventory_page.obtener_titulo() == "Products"


@pytest.mark.login
@pytest.mark.parametrize(
    "credenciales_login_invalido",
    DATOS_LOGIN_INVALIDO,
    ids=[datos["id"] for datos in DATOS_LOGIN_INVALIDO],
)
def test_login_fallido_con_credenciales_invalidas(
    driver,
    credenciales_login_invalido,
):
    """Valida distintos escenarios de login fallido usando datos externos."""
    login_page = LoginPage(driver)

    login_page.abrir().realizar_login(
        credenciales_login_invalido["usuario"],
        credenciales_login_invalido["password"],
    )

    assert login_page.hay_error_visible()

    mensaje_error = login_page.obtener_mensaje_error()

    assert credenciales_login_invalido["mensaje_esperado"] in mensaje_error
    assert "/inventory.html" not in driver.current_url