from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.page import loginPage

def test_login(driver, username, password):
    driver.find_element(*loginPage.findUsername).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, loginPage.passw).send_keys(password)
    driver.find_element(By.ID, loginPage.login_btn).click()