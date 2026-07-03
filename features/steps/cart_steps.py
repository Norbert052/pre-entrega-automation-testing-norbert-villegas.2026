from behave import given, when, then
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage


@given("que estoy autenticado en SauceDemo con usuario válido")
def step_given_authenticated_user(context):
    login_page = LoginPage(context.driver)
    login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.wait_until_loaded()


@when('agrego el producto "{product_name}" al carrito')
def step_when_add_product_to_cart(context, product_name):
    context.inventory_page.add_product_to_cart_by_name(product_name)
    context.inventory_page.open_cart()


@then('debo ver 1 producto en el carrito con nombre "{product_name}"')
def step_then_validate_product_in_cart(context, product_name):
    cart_page = CartPage(context.driver)
    cart_page.wait_until_loaded()
    assert cart_page.get_cart_items_count() == 1, "Expected 1 item in cart"
    assert cart_page.get_product_name() == product_name, f"Expected product name {product_name}"
