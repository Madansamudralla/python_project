from selenium import webdriver


class Firefox:

    def __init__(self, host, port):
        url = f"http://{host}:{port}/wd/hub"
        self.driver = webdriver.Remote(url, {"browserName": 'firefox'})
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()