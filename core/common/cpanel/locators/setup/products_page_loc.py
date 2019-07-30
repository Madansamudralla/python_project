from selenium.webdriver.common.by import By

class ProductsPageLocators:

    PAGE_TITLE = By.XPATH, "//h1[contains(text(),'Add product')]"
    ADD_NEW_PRODUCT = By.CLASS_NAME, 'call-to-action-label'

# Search products section
    PRODUCT_NAME = By.NAME, 'prod'
    PRODUCT_TYPE = By.NAME, 'productType'

    DISPLAY_ALL_PRODUCTS = By.ID, 'product_status_all'
    DISPLAY_ACTIVE_PRODUCTS = By.ID, 'product_status_enabled'
    DISPLAY_DISABLED_PRODUCTS = By.ID, 'product_status_disabled'
    SEARCH_PRODUCT_GROUP = By.ID, 'group'
    SEARCH_BUTTON = By.ID, 'search_products'


class AddProductPageLocators:
    # ADD PRODUCT PAGE
    # GENERAL
    ADD_PRODUCT_NAME = By.ID, 'productname'
    VERSION_MODEL = By.ID, 'productversion'
    PRODUCT_GROUP = By.ID, 'idgroup'
    EXTERNAL_REFERENCE = By.ID, 'externalReference'
    QUANTITY = By.ID, 'canPurchaseMoreThanOneProduct'
    PRODUCT_TYPE_REGULAR = By.ID, 'productIsbundle_No'
    PRODUCT_TYPE_BUNDLE = By.ID, 'productIsbundle_Yes'

    # PRICE
    DEFAULT_CURRENCY = By.ID, 'defaultIdCurrency'
    HAS_BASE_PRICE = By.ID, 'doesNotHaveBasePrice'
    PRICE = By.XPATH, '//*[contains(@id, "curr_")]'
    BILLING_CYCLE = By.ID, 'RenewalIntervalUnit'
    BILLING_CYCLE_UNITS = By.ID, 'RenewalIntervalAmount'
    CONVERT_CURRENCY_AUTO = By.ID, 'convert_currency'
    SET_CURRENCY_MANUALLY = By.ID, 'manual_currency'
    NET_PRICE = By.ID, 'net_price'
    GROSS_PRICE = By.ID, 'gross_price'

    # MARKETING DETAILS
    SHORT_DESC = By.ID, 'cke_1_contents'
    LONG_DESC = By.ID, 'cke_2_contents'

    CATEGORY = By.ID, 'categories'


    platforms = {
        "Android": "platf23",
        "BlackBerry": "platf25",
        "iPhone": "platf20",
        "J2ME": "platf24",
        "PalmOS": "platf7",
        "Symbian": "platf21",
        "Windows Mobile": "platf22",
        "Windows Phone": "platf27",
        "Windows RT": "platf28",
        "Beos": "platf9",
        "Dos": "platf10",
        "Fedora": "platf11",
        "FreeBSD": "platf13",
        "Linux": "platf4",
        "MacOS": "platf5",
        "OpenBSD": "platf14",
        "Windows 10": "platf32",
        "Windows 2000": "platf2",
        "Windows 7": "platf26",
        "Windows 8": "platf29",
        "Windows 9x": "platf1",
        "Windows NT": "platf3",
        "Windows Vista": "platf17",
        "Windows XP": "platf8",
        "Novell NetWare": "platf16",
        "Solaris": "platf15",
        "Unix": "platf6",
        "Windows Server 2003": "platf12",
        "Windows Server 2008": "platf18",
        "Windows Server 2008 R2": "platf30",
        "Windows Server 2012": "platf31",
        "Windows Server 2016": "platf33"
    }

    ADD_PRODUCT_SAVE = By.ID, 'AddProduct'
