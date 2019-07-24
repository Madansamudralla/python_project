from selenium.webdriver.common.by import By


class GapLoginPageLocators:

    USERNAME = By.ID, 'username'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'Login'

    # Dashboard changes
    MAINSCROLL_CONTAINER = By.LINK_TEXT, '_mainscroller_container'
