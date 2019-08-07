from selenium.webdriver.common.by import By


class GapOrdersSearchLocators:

    SEARCH_AFTER_SELECTOR = By.ID, 'tip'
    SEARCH_TEXT_TEXTFIELD = By.ID, 'search_text'
    STARTDATE_INPUT = By.ID, 'startdate'
    STARTDATE_TRIGGER_LINK = By.ID, 'trigger'
    ENDDATE_INPUT = By.ID, 'enddate'
    ENDDATE_TRIGGER_LINK = By.ID, 'trigger2'
    ADVANCED_SEARCH_LINK = By.ID, 'advancedHandleImage'
    SEARCH_BUTTON = By.CSS_SELECTOR, 'input[type=submit][value=Search]'
    WARNING_DISPLAY_DIV = By.LINK_TEXT, 'sphinx_warning'