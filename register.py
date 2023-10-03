import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.page import registerPage
from pageObject.data import inputan
from faker import Faker
#import baseLogin

fake = Faker()
fake_name = fake.name()
fake_email = fake.email()

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://demowebshop.tricentis.com/' 

    def test_a_page_title(self):
        driver = self.browser
        driver.get(self.url)
        self.assertIn('Demo Web Shop', self.browser.title)
        driver.quit()

    def test_b_go_to_register_page(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.quit()
    
    def test_b_success_register_female(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-female').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        get_url = driver.current_url
        self.assertIn('/registerresult/1', get_url)
        driver.find_element(By.CSS_SELECTOR, '.button-1.register-continue-button').click()
        driver.get(self.url)
        driver.quit()

    def test_b_success_register_male(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email2)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        get_url = driver.current_url
        self.assertIn('/registerresult/1', get_url)
        driver.find_element(By.CSS_SELECTOR, '.button-1.register-continue-button').click()
        driver.get(self.url)
        driver.quit()
    
    def test_c_failed_register_with_existing_email(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.registered_email)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '.validation-summary-errors li').text
        self.assertIn('The specified email already exists', error_message)
        driver.quit()

    def test_c_failed_register_email_without_domain(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.email_without_domain)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for] [for]').text
        self.assertIn('Wrong email', error_message)
        driver.quit()

    def test_c_failed_register_without_input_all_data(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type(2) > .form-fields > div:nth-of-type(2) > .field-validation-error').text
        self.assertIn('First name is required.', error_message)
        driver.quit()

    def test_c_failed_register_without_firstName(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]').text
        self.assertIn('First name is required.', error_message)
        driver.quit()
    
    def test_c_failed_register_without_lastName(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="LastName"]').text
        self.assertIn('Last name is required.', error_message)
        driver.quit()
    
    def test_c_failed_register_without_email(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Email"]').text
        self.assertIn('Email is required.', error_message)
        driver.quit()
    
    def test_c_failed_register_without_password(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email)
        driver.find_element(*registerPage.findConfirmPassword).send_keys(inputan.conf_password)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="Password"]').text
        self.assertIn('Password is required.', error_message)
        driver.quit()
    
    def test_c_failed_register_without_confirm_password(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]').text
        self.assertIn('Password is required.', error_message)
        driver.quit()
    
    def test_c_failed_register_password_is_not_match(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*registerPage.findRegisterTextLink).click()
        get_url = driver.current_url
        self.assertIn('/register', get_url)
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(*registerPage.findFirstName).send_keys(fake_name)
        driver.find_element(*registerPage.findLastName).send_keys(fake_name)
        driver.find_element(*registerPage.findRegisterEmail).send_keys(inputan.register_email)
        driver.find_element(*registerPage.findRegisterPassword).send_keys(inputan.password_regist)
        driver.find_element(*registerPage.findConfirmPassword).send_keys("testestes")
        driver.find_element(*registerPage.findRegisterButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]').text
        self.assertIn('The password and confirmation password do not match.', error_message)
        driver.quit()


if __name__ == '__main__':
    unittest.main()