from utils.driver_factory import get_driver


def before_scenario(context, scenario):
    context.driver = get_driver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
