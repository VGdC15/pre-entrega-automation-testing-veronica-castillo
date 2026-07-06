import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utils.data_reader import obtener_datos_prueba


@pytest.fixture(scope="function")
def driver():
    """Crea y cierra una instancia de Chrome WebDriver para cada test."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    navegador = webdriver.Chrome(service=service, options=chrome_options)

    yield navegador

    navegador.quit()


@pytest.fixture(scope="session")
def datos_prueba():
    """Carga los datos externos de prueba una sola vez por sesión."""
    return obtener_datos_prueba()


@pytest.fixture
def credenciales_validas(datos_prueba):
    """Devuelve credenciales válidas desde archivo JSON."""
    return datos_prueba["usuarios"]["valido"]


@pytest.fixture
def credenciales_invalidas(datos_prueba):
    """Devuelve el primer set de credenciales inválidas desde archivo JSON."""
    return datos_prueba["usuarios"]["invalidos"][0]


@pytest.fixture
def usuario_bloqueado(datos_prueba):
    """Devuelve el usuario bloqueado desde archivo JSON."""
    return datos_prueba["usuarios"]["invalidos"][1]


@pytest.fixture
def datos_checkout(datos_prueba):
    """Devuelve los datos de checkout desde archivo JSON."""
    return datos_prueba["checkout"]