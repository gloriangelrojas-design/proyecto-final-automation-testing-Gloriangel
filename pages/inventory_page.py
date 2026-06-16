from selenium.webdriver.common.by import By

class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def obtener_titulo(self):
        return self.driver.find_element(*self.TITLE).text

    def cantidad_productos(self):
        return len(self.driver.find_elements(*self.PRODUCTS))

    def agregar_producto(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def obtener_cantidad_carrito(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_LINK).click()

    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()