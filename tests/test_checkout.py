from utils.helpers import iniciar_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout():

    driver = iniciar_driver()

    try:

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.abrir()

        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        inventory_page.agregar_producto()
        inventory_page.ir_al_carrito()

        cart_page.checkout()

        checkout_page.completar_datos(
            "Cecilia",
            "Rojas",
            "1000"
        )

        assert "checkout-step-two" in driver.current_url

    finally:
        driver.quit()