from selenium.webdriver.common.by import By


class GapLoginPageLocators:

    # Login form locators

    USERNAME = By.ID, 'username'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'Login'

    # Dashboard changes
    SEARCH = By.ID, 'tiSearch'
