from utils.helpers import iniciar_driver
from pages.login_page import LoginPage

def test_login_invalido():

    driver = iniciar_driver()

    login_page = LoginPage(driver)

    login_page.abrir()

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    assert "Epic sadface" in login_page.obtener_error()

    driver.quit()