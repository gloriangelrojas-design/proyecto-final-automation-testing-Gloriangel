from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def completar_datos(self, nombre, apellido, codigo):

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(nombre)

        self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        ).send_keys(apellido)

        self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        ).send_keys(codigo)

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()