from selenium.webdriver.common.by import By


class FulfillmentPage:


# ELECTRONIC_DELIVERY_TAB
    PAGE_TITLE = By.TAG_NAME("Electronic delivery")
    ELECTRONIC_DELIVERY_TAB = By.ID, '__tab_Electronic_delivery'

# Tab elements
    LIST_NAME = By.ID, 'listname'
    LIST_TYPE = By.ID, 'listtype'


# DOWNLOAD_INSURANCE_TAB
    DOWNLOAD_INSURANCE_TAB = By.ID, '__tab_Download_insurance'

# Tab elements


# BACKUP_MEDIA_TAB
    BACKUP_MEDIA_TAB = By.ID, '__tab_Backup_media'

# Tab elements

# SHIPPING_FEES_TAB
    SHIPPING_FEES_TAB = By.ID, '__tab_Shipping_fees'
    SHIPPING_CLASSES = By.ID, 'Shipping classes'
    DELIVERY_ZONES = By.ID, 'Delivery zones »'

    SHIPPING_FEE_NAME = By.ID, 'name0'
    COST_TYPE = By.NAME, 'pricetype0'
    PRICE_VALUE = By.NAME, 'shipprice0'
    SHIPPING_TYPE = By.NAME, 'priceapply0'


# SHIPPING_CLASSES_PAGE
    CLASS_NAME =  By.ID, 'shipname'
    PRICE = By.ID, 'shipprice'
    CURRENCY = By.ID, 'idcurrency_add'
    TYPE = By.ID, 'pricetype'
    ADD_BUTTON = By.ID, 'AddShipPrice'
    BACK_BUTTON = By.LINK_TEXT, 'Back'

# DELIVERY ZONES PAGE

# Tab elements


# SHIPPING_METHODS_TAB
    SHIPPING_METHODS_TAB = By.ID, '__tab_Shipping_methods'

# Tab elements
    ADD_SHIPPING_METHOD = By.ID, 'shipping_method_name'
    TRACKING_URL = By.ID, 'tracking_url'
    ADD_SHIPPING_METHOD_BUTTON = By.ID, 'AddShippingMethod'
    ACTIVATE_BUTTON = By.ID, 'activate'
    DEACTIVATE_BUTTON = By.ID, 'deactivate'




# PRODUCT_FILES_TAB
    PRODUCT_FILES_TAB = By.ID, '__tab_Product_files'

# Tab elements
    ADD_NEW_PRODUCT_FILE = By.ID, 'displayname'
    FILE_VERSION = By.ID, 'fileversion'
    BROWSE_FILE = By.ID, 'uploadfile'
    UPLOAD_FILE = By.ID, 'addfile'
