# SauceDemo Automation Project

Proyecto de automatizacion web para probar el sitio SauceDemo usando Python, Selenium WebDriver y Pytest.

## Descripcion

Este proyecto contiene tests automatizados que validan la funcionalidad principal del sitio https://www.saucedemo.com. Los tests incluyen login, validacion del catalogo de productos y funcionalidad del carrito de compras.

## Tecnologias

- Python 3.13+
- Selenium 4.15.2
- Pytest 7.4.3
- webdriver-manager 4.0.1
- pytest-html 4.1.1

## Instalacion

1. Clonar o descargar el proyecto

2. Crear un entorno virtual (opcional pero recomendado)
   python -m venv venv
   venv\Scripts\activate

3. Instalar dependencias
   pip install -r requirements.txt

## Ejecutar los tests

Ejecutar todos los tests
   pytest

Ejecutar un test especifico
   pytest tests/test_saucedemo.py::TestSauceDemo::test_login_successful

Ejecutar con modo verbose
   pytest -v

Generar reporte HTML
   pytest --html=reports/report.html --self-contained-html

## Tests implementados

1. test_login_successful: Valida el login con usuario standard_user

2. test_catalog_elements: Valida que la pagina de catalogo muestre productos, menu y filtro

3. test_add_to_cart: Valida agregar un producto al carrito y su visualizacion

## Estructura del proyecto

tests/
  test_saucedemo.py - Archivo con todos los tests
  conftest.py - Configuracion de pytest

utils/
  driver_factory.py - Configuracion y creacion del WebDriver
  helpers.py - Funciones auxiliares para acciones comunes

reports/
  report.html - Reporte HTML generado por pytest-html
  screenshots/ - Capturas de pantalla en caso de fallos

## Notas

- Los tests son independientes entre si
- Se utilizan WebDriverWait en lugar de time.sleep
- Las capturas de pantalla se generan automaticamente en caso de fallo
- El driver Chrome se abre maximizado
- Se incluyen opciones para evadir deteccion de automatizacion

## Contacto

Para preguntas o mejoras, contactar al equipo de QA.