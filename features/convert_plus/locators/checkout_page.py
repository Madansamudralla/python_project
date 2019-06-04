from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    THANK_YOU_MESSAGE_LOCATOR = By.CLASS_NAME, 'order-top-message'
    FINISH_PAGE_REFERENCE_NUMBER_LOCATOR = By.CLASS_NAME, 'info-value'
    PANEL_CONFIRMATION_EMAIL_LOCATOR = By.CLASS_NAME, 'confirmation-email'

    LOADER_CLASS_BUSY = By.CLASS_NAME, 'nprogress-busy'
    LOADER_CLASS_LOCATOR = By.CLASS_NAME, 'ajax-loader'

    LOADER_DELETE_ITEM = By.CSS_SELECTOR = '.cart-items .ajax-loader'

    CITY = By.ID, 'city'

    COUNTRY_INPUT_LOCATOR = By.CLASS_NAME, 'dropdown-country'
    COUNTRY_INPUT_FIELD = By.ID, 'dropdown-multiselect-country'

    # Payment form elements

    CARD_NUMBER_INPUT_LOCATOR = By.ID, 'card'
    CARD_EXPIRATION_DATE_INPUT_LOCATOR = By.ID, 'date'
    CARD_SECURITY_CODE_INPUT_LOCATOR = By.ID, 'cvv'
    NAME_INPUT_LOCATOR = By.ID, 'name'

    # Billing form elements
    EMAIL_INPUT_LOCATOR = By.ID, 'email'

    # Checkout button elements
    PLACE_ORDER_BUTTON_LOCATOR = By.CLASS_NAME, 'btn-pay'
