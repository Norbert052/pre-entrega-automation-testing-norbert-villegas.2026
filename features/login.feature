Feature: Login en SauceDemo
  Como usuario de SauceDemo
  Quiero iniciar sesión para acceder al catálogo de productos

  Background:
    Given que estoy en la página de login de SauceDemo

  @login @positivo @regression
  Scenario: Login exitoso
    When ingreso las credenciales válidas
    Then debo ver la página de inventario con el título "Products"

  @login @negativo
  Scenario Outline: Login inválido con datos de ejemplo
    When ingreso usuario "<username>" y contraseña "<password>"
    Then debo ver un mensaje de error de inicio de sesión

    Examples:
      | username       | password       |
      | standard_user  | wrong_password |
      | locked_out_user| secret_sauce   |
