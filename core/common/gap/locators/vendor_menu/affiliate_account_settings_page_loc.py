from selenium.webdriver.common.by import By


class AffiliateAccountSettingsPageLocators:

    # Active payout methods and associated affiliate fees
    PAYOUT_METHOD_SELECTED_BY_AFFILIATE_SELECT = By.ID, 'IdAffiliatePaymentSettings'
    SOCRATE_CODE_INPUT = By.NAME, 'CodSocrate'
    PAYOUT_CURRENCY_SELECT = By.NAME, 'currency'
    PAYOUT_THRESHOLD_INPUT = By.NAME, 'min_balance'
    SAVE_BUTTON = By.CLASS_NAME, 'Update'
