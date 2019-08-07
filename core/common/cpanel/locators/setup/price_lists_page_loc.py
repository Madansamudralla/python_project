from selenium.webdriver.common.by import By

class PriceListsPage:

# ADD PRICE LIST page
    PRICE_LIST_NAME = By.ID, 'listName'
    DESCRIPTION = By.ID, 'listDescription'
    SEARCH_BOTH_SIDES = By.ID, 'master_filter'
    SAVE_BUTTON = By.NAME, 'saveList'

# PRICE LISTS page
    ADD_PRICE_LIST = By.LINK_TEXT, 'Add price list'
