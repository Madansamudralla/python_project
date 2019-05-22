import automation_cnf


class Config:

    # Browser and Selenium setup
    MY_BROWSER = "chrome"
    SELENIUM_HOST = "localhost"
    SELENIUM_PORT = 4444

    # Database environment settings
    DB_ENVIRONMENT = 'automation'

    # URL configuration settings
    BASE_URL = "http://" + automation_cnf.MY_HOST_NAME + ".avangate.local"
    SHORT_BASE_URL = "http://" + automation_cnf.MY_HOST_NAME + ".avangate.local/l.php?link="
    BASE_URL_INDEPENDENT = "http://processing." + automation_cnf.MY_HOST_NAME + ".avangate.local"
    API_URL = "http://api." + automation_cnf.MY_HOST_NAME + ".avangate.local"
    API_CART_URL = "http://cart." + automation_cnf.MY_HOST_NAME + ".avangate.local"
    SIGNUP_API_URI = BASE_URL + "/api/private/2.5/rpc/"
    IMPORT_MERCHANT_API_URI = BASE_URL + "/apimigration/"

    # Cron running configuration
    CRON_HOST = automation_cnf.CRON_SANDBOX + ".avangate.local"
    CRON_PATH = "/var/www/vhosts/" + automation_cnf.CRON_SANDBOX + ".avangate.local/htdocs/cron/"
    CRON_PATH_CUSTOMCARTS = "/var/www/stage.sandbox/htdocs/cron/"
    CRON_USER = "www-data"

    USER = "automation"
    PUBLIC_KEY = "/home/automation/www/automation/conf/automation_publicOpen"
    PRIVATE_KEY = "/home/automation/www/automation/conf/automation_privateOpen"
