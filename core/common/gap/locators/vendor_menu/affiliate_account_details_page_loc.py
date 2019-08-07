from selenium.webdriver.common.by import By


class AffiliateAccountDetailsPageLocators:

    CONTRACT_DATE_INPUT = By.ID, 'contractdate'
    VAT_ID_NO_INPUT = By.NAME, 'fiscalcode'
    BUSSINESS_COMPANY_SELECT = By.NAME, 'IdBusinessCompanies'
    BAN_ACCOUNT_BUTTON = By.CSS_SELECTOR, '// *[ @ value = "Ban account" and @type="button"]'
    DEACTIVATE_ACCOUNT_BUTTON = By.CSS_SELECTOR, '// *[ @ value = "Deactivate account" and @type="button"]'
    SAVE_BUTTON = By.CSS_SELECTOR, '// *[ @ value = "Save" and @type="submit"]'
