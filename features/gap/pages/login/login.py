from .elements import LoginPage


class LoginTest:

    def __init__(self, context):
        self.driver = context.driver

    def login(self, username, password):
        loginform = LoginPage(self.driver)
        loginform.navigate()
        loginform.setUserName(username)
        loginform.setPassword(password)
        loginform.submit()
