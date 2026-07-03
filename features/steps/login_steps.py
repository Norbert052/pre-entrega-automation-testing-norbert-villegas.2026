from behave import given, when, then
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from utils.helpers import get_text, wait_for_visibility


@given("que estoy en la página de login de SauceDemo")
def step_given_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when("ingreso las credenciales válidas")
def step_when_enter_valid_credentials(context):
    context.login_page.login("standard_user", "secret_sauce")


@when('ingreso usuario "{username}" y contraseña "{password}"')
def step_when_enter_invalid_credentials(context, username, password):
    context.login_page.login(username, password)


@then('debo ver la página de inventario con el título "{expected_title}"')
def step_then_inventory_page_title(context, expected_title):
    inventory_page = InventoryPage(context.driver)
    wait_for_visibility(context.driver, inventory_page.TITLE)
    actual_title = inventory_page.get_title()
    assert actual_title == expected_title, f"Expected title {expected_title}, got {actual_title}"


@then("debo ver un mensaje de error de inicio de sesión")
def step_then_login_error_message(context):
    error_message = context.login_page.get_error_message()
    assert error_message, "Expected an error message for invalid login"
