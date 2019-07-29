from selenium.webdriver.common.by import By


class CpanelLoginPageLocators:

    USERNAME = By.ID, 'email'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'Login'
    DASHBOARD = By.ID, 'page-title'
