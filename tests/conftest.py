import os

import pytest
from utils.helpers import take_screenshot
from utils.logger import logger


def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    logger.info("Inicio de ejecución de pruebas")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and call.when == "call":
        driver = None
        if hasattr(item, "instance") and hasattr(item.instance, "driver"):
            driver = item.instance.driver
        elif hasattr(item, "funcargs") and "setup_teardown" in item.funcargs:
            setup = item.funcargs["setup_teardown"]
            if setup is not None and hasattr(setup, "driver"):
                driver = setup.driver
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            logger.error("Captura de pantalla guardada: %s", screenshot_path)
        else:
            logger.error("Fallo en prueba sin driver: %s", item.name)


def pytest_runtest_logreport(report):
    if report.failed and report.when == "call":
        logger.error("Prueba fallida: %s", report.nodeid)
