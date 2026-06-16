from utils.helpers import iniciar_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_carrito():

    driver = iniciar_driver()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.abrir()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.agregar_producto()

    assert inventory_page.obtener_cantidad_carrito() == "1"

    inventory_page.ir_al_carrito()

    assert cart_page.producto_visible() is not None

    driver.quit()