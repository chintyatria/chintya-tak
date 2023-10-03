import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.page import loginPage
from pageObject.page import addCart
from pageObject.data import inputan


class AddToCartTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://demowebshop.tricentis.com/' 

    def test_a_page_title(self):
        driver = self.browser
        driver.get(self.url)
        self.assertIn('Demo Web Shop', self.browser.title)
        driver.quit()

    def test_b_success_add_to_cart(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(*loginPage.findLoginTextLink).click()
        get_url = driver.current_url
        self.assertIn('/login', get_url)
        driver.find_element(*loginPage.findLoginEmail).send_keys(inputan.email_login)
        driver.find_element(*loginPage.findLoginPassword).send_keys(inputan.password_login)
        driver.find_element(*loginPage.findLoginButton).click()
        driver.get(self.url)
        driver.find_element(*addCart.findMainMenuButton).click()
        get_url = driver.current_url
        self.assertIn('/computers', get_url)
        driver.find_element(*addCart.findSubMenuButton).click()
        get_url = driver.current_url
        self.assertIn('/notebooks', get_url)
        driver.find_element(*addCart.add_to_cart_button).click()
        success_message = driver.find_element(By.CSS_SELECTOR, '.content').text
        self.assertIn('The product has been added to your ', success_message)
        cart = driver.find_element(By.CLASS_NAME, 'ico-cart').text
        self.assertEqual(cart, '1')
        driver.quit()


if __name__ == '__main__':
    unittest.main()