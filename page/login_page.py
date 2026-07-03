from selenium.webdriver.common.by import By
from utils.helpers import click_element, fill_text, get_text, wait_for_visibility
from utils.logger import logger


class LoginPage:
    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def ingresar_usuario(self, usuario):
        fill_text(self.driver, self.USERNAME, usuario)

    def ingresar_password(self, password):
        fill_text(self.driver, self.PASSWORD, password)

    def click_login(self):
        click_element(self.driver, self.LOGIN_BUTTON)

    def login(self, usuario, password):
        logger.info("Login con usuario: %s", usuario)
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def get_error_message(self):
        try:
            error_text = get_text(self.driver, self.ERROR_MESSAGE)
            logger.info("Mensaje de error en login: %s", error_text)
            return error_text
        except Exception as exc:
            logger.error("No se encontró mensaje de error de login: %s", exc)
            return ""
