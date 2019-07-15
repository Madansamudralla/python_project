from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    THANK_YOU_MESSAGE_LOCATOR = By.CLASS_NAME, 'order-top-message'
    FINISH_PAGE_REFERENCE_NUMBER_LOCATOR = By.CLASS_NAME, 'info-value'
    PANEL_CONFIRMATION_EMAIL_LOCATOR = By.CLASS_NAME, 'confirmation-email'

    LOADER_CLASS_BUSY = By.CLASS_NAME, 'nprogress-busy'
    LOADER_CLASS_LOCATOR = By.CLASS_NAME, 'ajax-loader'

    LOADER_DELETE_ITEM = By.CSS_SELECTOR = '.cart-items .ajax-loader'

    COUNTRY_INPUT_LOCATOR = By.CLASS_NAME, 'dropdown-country'
    COUNTRY_INPUT_FIELD = By.ID, 'dropdown-multiselect-country'

    # Payment form elements
    CARD_NUMBER_INPUT_LOCATOR = By.ID, 'card'
    CARD_EXPIRATION_DATE_INPUT_LOCATOR = By.ID, 'date'
    CARD_SECURITY_CODE_INPUT_LOCATOR = By.ID, 'cvv'
    NAME_INPUT_LOCATOR = By.ID, 'name'
    IBAN_INPUT_LOCATOR = By.ID, 'iban'
    SWIFT_CODE_INPUT_LOCATOR = By.ID, 'swift-code'

    # Billing form elements
    EMAIL_INPUT_LOCATOR = By.ID, 'email'
    ADDRESS_INPUT_LOCATOR = By.ID, 'address'
    CITY_INPUT_LOCATOR = By.ID, 'city'
    ZIP_INPUT_LOCATOR = By.ID, 'zip'
    PHONE_INPUT_LOCATOR = By.ID, 'phone'

    # Checkout button elements
    PLACE_ORDER_BUTTON_LOCATOR = By.CLASS_NAME, 'btn-pay'
    OTHER_BUTTON = By.LINK_TEXT, 'Other'

    # Payment method elements
    PAYMENT_METHOD_DIRECT_DEBIT_LOCATOR = By.LINK_TEXT, 'SEPA Direct Debit'
    PAYMENT_METHOD_WIRE_TRANSFER_LOCATOR = By.LINK_TEXT, 'Wire Transfer'
    PAYMENT_METHOD_PAYPAL_LOCATOR = By.LINK_TEXT, 'PayPal'
    # PAYMENT_METHOD_PAYPAL_LOCATOR = By.CSS_SELECTOR, '.default-button.add-tooltip.paypal'
