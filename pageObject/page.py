from selenium.webdriver.common.by import By

class registerPage():
    register_text_link = 'ico-register'
    genderMale = 'gender-male'
    genderFemale = 'gender-female'
    firstName = 'FirstName'
    lastName = 'LastName'
    register_email = 'Email'
    register_password = 'Password'
    confpassword = 'ConfirmPassword'
    register_btn = 'register-button'
    continue_register = '.button-1.register-continue-button'

    findRegisterTextLink = (By.CLASS_NAME, 'ico-register')
    findFirstName = (By.ID, 'FirstName')
    findLastName = (By.ID, 'LastName')
    findRegisterEmail = (By.ID, 'Email')
    findRegisterPassword = (By.ID, 'Password')
    findConfirmPassword = (By.ID, 'ConfirmPassword')
    findRegisterButton = (By.ID, 'register-button')
    findContinueRegister = (By.CSS_SELECTOR, '.button-1.register-continue-button')

class loginPage():
    login_text_link = 'ico-login'
    login_email = 'Email'
    login_password = 'Password'
    login_btn = '.button-1.login-button'

    findLoginTextLink = (By.CLASS_NAME, 'ico-login')
    findLoginEmail = (By.ID, 'Email')
    findLoginPassword = (By.ID, 'Password')
    findLoginButton = (By.CSS_SELECTOR, '.button-1.login-button')

class addCart():
    main_menu_button = 'COMPUTERS'
    sub_menu_button = '.sub-category-grid > div:nth-of-type(2)'
    add_to_cart_button = '.button-2.product-box-add-to-cart-button'
    notification = ".content"

    findMainMenuButton = (By.LINK_TEXT, 'COMPUTERS')
    findSubMenuButton = (By.CSS_SELECTOR, '.sub-category-grid > div:nth-of-type(2)')
    findAddToCartButton = (By.CLASS_NAME, '.button-2.product-box-add-to-cart-button')
    findNotification = (By.CSS_SELECTOR, '.content')