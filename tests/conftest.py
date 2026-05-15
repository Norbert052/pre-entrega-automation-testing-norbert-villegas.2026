import pytest
from utils.helpers import take_screenshot


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.failed and call.when == "call":
        if hasattr(item, "funcargs") and "setup_teardown" in item.funcargs:
            driver = item.funcargs["setup_teardown"].driver
            if driver:
                take_screenshot(driver, item.name)
