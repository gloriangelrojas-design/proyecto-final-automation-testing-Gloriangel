from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def esperar_elemento(driver, by, locator):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, locator))
    )