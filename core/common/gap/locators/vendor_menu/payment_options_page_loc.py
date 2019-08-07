from selenium.webdriver.common.by import By


class PaymentOptionsPageLocators:

    VISA_MASTERCARD_EN_DB_SELECT = By.ID, 's2id_autogen1'
    VISA_MASTERCARD_EN_DB_STATUS_CHECKBOX = By.NAME, 'poStatusFacade[1]'
    BANK_WIRE_TRANSFER_ECOMMERCE_SELECT = By.ID, 's2id_autogen5'
    BANK_WIRE_TRANSFER_ECOMMERCE_STATUS_CHECKBOX = By.NAME, 'poStatusFacade[2]'
    BANK_WIRE_TRANSFER_ARMS_RS_SELECT = By.ID, 's2id_autogen121'
    BANK_WIRE_TRANSFER_ARMS_RS__STATUS_CHECKBOX = By.NAME, 'poStatusFacade[26]'
    SAVE_BUTTON = By.NAME, 'save_changes'
