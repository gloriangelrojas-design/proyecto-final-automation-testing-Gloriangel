from utils.helpers import iniciar_driver
from pages.login_page import LoginPage

def test_login_exitoso():

    driver = iniciar_driver()

    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    driver.quit()