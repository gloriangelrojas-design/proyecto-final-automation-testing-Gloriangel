from selenium.webdriver.common.by import By
from utils.helpers import iniciar_driver, login, esperar_elemento


def test_login():
    driver = iniciar_driver()
    login(driver)

    esperar_elemento(driver, By.CLASS_NAME, "title")

    assert "inventory.html" in driver.current_url
    assert "Swag Labs" in driver.page_source

    driver.quit()


def test_catalogo():
    driver = iniciar_driver()
    login(driver)

    titulo = esperar_elemento(driver, By.CLASS_NAME, "title")
    assert titulo.text == "Products"

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0

    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    print(nombre, precio)

    driver.quit()


def test_carrito():
    driver = iniciar_driver()
    login(driver)

    driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()

    badge = esperar_elemento(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    item = esperar_elemento(driver, By.CLASS_NAME, "inventory_item_name")
    assert item is not None

    driver.quit()