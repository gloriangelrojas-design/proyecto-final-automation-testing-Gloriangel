from utils.helpers import iniciar_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_catalogo():

    driver = iniciar_driver()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.abrir()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.cantidad_productos() > 0

    driver.quit()