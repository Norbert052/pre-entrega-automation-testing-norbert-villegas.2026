Feature: Carrito de compras en SauceDemo
  Como usuario autenticado
  Quiero agregar un producto al carrito y validarlo

  @cart @regression
  Scenario: Agregar un producto al carrito y validar su presencia
    Given que estoy autenticado en SauceDemo con usuario válido
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then debo ver 1 producto en el carrito con nombre "Sauce Labs Backpack"
