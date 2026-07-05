# Framework de Automatización QA

Framework de automatización de pruebas desarrollado sobre SauceDemo para las pruebas de interfaz y JSONPlaceholder para las pruebas de API. El proyecto integra automatización UI con Selenium, pruebas de API con Requests y escenarios BDD con Behave, además de reportes HTML, logging y capturas automáticas.

## Tecnologías utilizadas

| Tecnología |
| --- |
| Python |
| Selenium |
| Pytest |
| Requests |
| Behave |
| Gherkin |
| pytest-html |
| webdriver-manager |
| GitHub Actions |

## Estructura del proyecto

```
README.md
requirements.txt
pytest.ini
.github/
  workflows/
    ci.yml
data/
  login.csv
  products.json
features/
  login.feature
  cart.feature
  environment.py
  steps/
    login_steps.py
    cart_steps.py
page/
  login_page.py
  inventory_page.py
  cart_page.py
tests/
  conftest.py
  test_saucedemo.py
tests_api/
  test_api_posts.py
utils/
  data_reader.py
  driver_factory.py
  helpers.py
  logger.py
reports/
  report.html
logs/
screenshots/
```

## Arquitectura

El proyecto utiliza Page Object Model en `page/`. Cada clase de página encapsula selectores y acciones de SauceDemo. Los tests usan esas clases para ejecutar flujos sin repetir la lógica de UI.

## Instalación

```bash
git clone https://github.com/Norbert052/proyecto-final-automation-testing-norbert-villegas.git
cd proyecto-final-automation-testing-norbert-villegas
pip install -r requirements.txt
```

## Ejecución

```bash
python -m pytest
python -m pytest tests/
python -m pytest tests_api/
python -m behave
python -m pytest --html=reports/report.html --self-contained-html
```

## Pruebas implementadas

### UI

- `tests/test_saucedemo.py::TestSauceDemo::test_login`
- `tests/test_saucedemo.py::TestSauceDemo::test_catalog_elements`
- `tests/test_saucedemo.py::TestSauceDemo::test_add_to_cart`

### API

- `tests_api/test_api_posts.py::test_get_post_by_id`
- `tests_api/test_api_posts.py::test_create_post`
- `tests_api/test_api_posts.py::test_delete_post`

### BDD

- `features/login.feature`
- `features/cart.feature`

## Datos de prueba

- `data/login.csv` contiene las credenciales y el resultado esperado para los escenarios de login.
- `data/products.json` contiene productos usados por los tests de carrito.

## Reportes

- `reports/report.html` es el reporte generado por `pytest-html`.
- `screenshots/` almacena capturas automáticas de fallos.
- `logs/automation.log` contiene registros de ejecución.

## Integración continua

El proyecto utiliza GitHub Actions para ejecutar automáticamente la suite y publicar artefactos de `reports`, `screenshots` y `logs/automation.log`.

## Resultado

El framework permite ejecutar pruebas UI, pruebas API y escenarios BDD, generar reportes HTML, registrar logs y capturar fallos automáticamente.
