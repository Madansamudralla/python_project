import paramiko
from selenium import webdriver
import conf


class set_up:
    def web_set_up(self, browser):
        if browser == "chrome":
            driver = webdriver.Chrome(conf.Chrome)
            return driver

    def cron_setup(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(conf.CRON_HOST, 22, conf.USER, conf.key)
        return client

