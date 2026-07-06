# Framework de Automatización de Pruebas - SauceDemo

Proyecto de automatización de pruebas desarrollado en Python con Pytest, Selenium WebDriver y Requests.

El objetivo del framework es validar flujos principales de una aplicación web demo tipo e-commerce, aplicando buenas prácticas de automatización, patrón Page Object Model, pruebas de UI, pruebas de API, reportes HTML, screenshots automáticos ante fallos y logging centralizado.

---

## Aplicación bajo prueba

**SauceDemo**  
https://www.saucedemo.com/

SauceDemo es una aplicación demo de e-commerce utilizada para practicar automatización de pruebas. Permite validar escenarios como login, catálogo de productos, carrito y checkout.

---

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- Page Object Model
- Git / GitHub
- JSON para datos externos
- Logging nativo de Python

---

## Estructura del proyecto

```txt
pre-entrega-automation-testing-veronica-castillo/
├── data/
│   └── test_data.json
├── logs/
│   └── .gitkeep
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── reports/
│   └── .gitkeep
├── screenshots/
│   └── .gitkeep
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_catalogo.py
│   ├── test_carrito.py
│   └── test_checkout.py
├── tests_api/
│   ├── __init__.py
│   └── test_posts_api.py
├── utils/
│   ├── __init__.py
│   ├── data_reader.py
│   └── logger_config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Patrón Page Object Model

El proyecto implementa Page Object Model para separar la lógica de interacción con la interfaz de la lógica de validación de los tests.

Cada página de SauceDemo está representada por una clase:

```txt
LoginPage       → Login
InventoryPage   → Catálogo de productos
CartPage        → Carrito de compras
CheckoutPage    → Flujo de checkout
```

Los archivos dentro de `pages/` contienen:

- Locators centralizados.
- Métodos de acción.
- Métodos de lectura de información.
- Esperas explícitas.
- Navegación entre páginas.

Los archivos dentro de `tests/` contienen:

- Casos de prueba.
- Assertions.
- Validaciones de resultados esperados.

---

## Casos de prueba UI

La suite de UI cubre los siguientes escenarios:

| Archivo | Caso |
|---|---|
| `tests/test_login.py` | Login exitoso |
| `tests/test_login.py` | Login fallido con credenciales inválidas |
| `tests/test_login.py` | Login fallido con usuario bloqueado |
| `tests/test_catalogo.py` | Validación del catálogo luego del login |
| `tests/test_carrito.py` | Agregar producto al carrito |
| `tests/test_checkout.py` | Flujo completo de checkout |

---

## Casos de prueba API

La suite de API utiliza JSONPlaceholder:

https://jsonplaceholder.typicode.com/

Casos incluidos:

| Archivo | Método | Validación |
|---|---:|---|
| `tests_api/test_posts_api.py` | GET | Obtener un post existente |
| `tests_api/test_posts_api.py` | POST | Crear un post simulado |
| `tests_api/test_posts_api.py` | DELETE | Eliminar un post simulado |

Las pruebas validan:

- Código de estado HTTP.
- Estructura de la respuesta JSON.
- Contenido esperado.
- Tipos de datos principales.

---

## Datos externos

Los datos de prueba se leen desde:

```txt
data/test_data.json
```

Este archivo contiene:

- Credenciales válidas.
- Credenciales inválidas.
- Usuario bloqueado.
- Datos para checkout.

Ejemplo:

```json
{
  "usuarios": {
    "valido": {
      "usuario": "standard_user",
      "password": "secret_sauce"
    }
  }
}
```

La lectura se centraliza en:

```txt
utils/data_reader.py
```

---

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/VGdC15/pre-entrega-automation-testing-veronica-castillo.git
```

### 2. Ingresar al proyecto

```bash
cd pre-entrega-automation-testing-veronica-castillo
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

En Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

En Windows CMD:

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de pruebas

### Ejecutar toda la suite

```bash
python -m pytest
```

### Ejecutar solo pruebas UI

```bash
python -m pytest tests
```

### Ejecutar solo pruebas API

```bash
python -m pytest tests_api
```

### Ejecutar pruebas por marker

Login:

```bash
python -m pytest -m login
```

Catálogo:

```bash
python -m pytest -m catalogo
```

Carrito:

```bash
python -m pytest -m carrito
```

Checkout:

```bash
python -m pytest -m checkout
```

API:

```bash
python -m pytest -m api
```

---

## Reportes HTML

El proyecto utiliza `pytest-html`.

La configuración está en:

```txt
pytest.ini
```

Cada ejecución genera un reporte en:

```txt
reports/report.html
```

Para abrirlo, ingresar a la carpeta `reports/` y abrir el archivo `report.html` en el navegador.

El reporte muestra:

- Tests ejecutados.
- Estado de cada test.
- Duración.
- Errores.
- Screenshots asociados a fallos, cuando corresponda.

---

## Screenshots automáticos

Cuando un test falla, el framework captura automáticamente una pantalla del navegador y la guarda en:

```txt
screenshots/
```

El nombre del archivo incluye:

- Fecha.
- Hora.
- Nombre del test.

Ejemplo:

```txt
screenshots/20260706_203310_test_checkout_completo.png
```

Los screenshots se generan como evidencia de fallos, pero no se versionan en Git.

---

## Logging

El proyecto implementa logging centralizado mediante el módulo nativo `logging`.

Configuración:

```txt
utils/logger_config.py
```

Archivo generado:

```txt
logs/automation.log
```

El log registra:

- Inicio y fin de la suite.
- Inicio de cada test.
- Tests exitosos.
- Tests fallidos.
- Creación y cierre del navegador.
- Capturas de pantalla generadas ante fallos.

Los archivos `.log` no se versionan en Git.

---

## Configuración de Pytest

El archivo `pytest.ini` centraliza:

- Opciones de ejecución.
- Generación automática del reporte HTML.
- Registro de markers personalizados.

Markers disponibles:

```txt
login
catalogo
carrito
checkout
api
```

---

## Buenas prácticas aplicadas

- Separación entre tests y lógica de página.
- Uso de Page Object Model.
- Locators centralizados.
- Esperas explícitas.
- Fixtures reutilizables en `conftest.py`.
- Datos externos en JSON.
- Parametrización de escenarios negativos.
- Screenshots automáticos en fallos.
- Logging centralizado.
- Reporte HTML automático.
- Tests independientes entre sí.
- Control de versiones con commits incrementales.

---

## Estado actual de la suite

La suite incluye:

```txt
6 pruebas UI
3 pruebas API
9 pruebas automatizadas en total
```

---

## Autor

**Verónica Lía Castillo**

GitHub: https://github.com/VGdC15  
Portfolio: https://veronica-castillo.vercel.app/  
LinkedIn: https://www.linkedin.com/in/veronica-l-castillo