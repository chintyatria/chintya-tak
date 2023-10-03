import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.page import loginPage
from pageObject.data import inputan


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://demowebshop.tricentis.com/' 

    def test_a_page_title(self):
        driver = self.browser
        driver.get(self.url)
        self.assertIn('Demo Web Shop', self.browser.title)
        driver.quit()

    def test_b_go_to_login_page(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.quit()

    def test_b_success_login(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginEmail).send_keys(inputan.email_login)
        driver.find_element(*loginPage.findLoginPassword).send_keys(inputan.password_login)
        driver.find_element(*loginPage.findLoginButton).click()
        driver.get(self.url)
        driver.quit()

    def test_c_failed_login_with_unregistered_email(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginEmail).send_keys('chinchinchin@gmail.com')
        driver.find_element(*loginPage.findLoginPassword).send_keys(inputan.password_login)
        driver.find_element(*loginPage.findLoginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors li').text
        self.assertIn('No customer account found', error_message)
        driver.quit()

    def test_c_failed_login_with_unregistered_password(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginEmail).send_keys(inputan.email_login)
        driver.find_element(*loginPage.findLoginPassword).send_keys('iniadapassword')
        driver.find_element(*loginPage.findLoginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors li').text
        self.assertIn('The credentials provided are incorrect', error_message)
        driver.quit()
    
    def test_c_failed_login_with_unregistered_account(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginEmail).send_keys('itseasy@gmail.com')
        driver.find_element(*loginPage.findLoginPassword).send_keys('thisispassword')
        driver.find_element(*loginPage.findLoginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors li').text
        self.assertIn('No customer account found', error_message)
        driver.quit()

    def test_c_failed_login_without_email(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginPassword).send_keys(inputan.password_login)
        driver.find_element(*loginPage.findLoginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors li').text
        self.assertIn('No customer account found', error_message)
        driver.quit()

    def test_c_failed_login_without_password(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginEmail).send_keys(inputan.email_login)
        driver.find_element(*loginPage.findLoginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors li').text
        self.assertIn('The credentials provided are incorrect', error_message)
        driver.quit()
        
    def test_c_failed_login_without_input_data(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors').text
        self.assertIn('Login was unsuccessful. Please correct the errors and try again.', error_message)
        driver.quit()

if __name__ == '__main__':
    unittest.main()