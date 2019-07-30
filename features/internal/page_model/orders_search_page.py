from selenium.webdriver.common.keys import Keys
from features.internal.locators.orders_search_page_loc import GapOrdersSearchLocators
import core


class GapOrdersSearch:

        def __init__(self, host):
            self.host = host
            self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

        def enter_a_text_to_search(self, textfield):
            """Method  to search a order after a text

            returns:
                That searched order
            """
            self.driver.find_element(*GapOrdersSearchLocators.SEARCH_TEXT_TEXTFIELD).send_keys(Keys.CLEAR)
            self.driver.find_element(*GapOrdersSearchLocators.SEARCH_TEXT_TEXTFIELD).send_keys(textfield)
            self.driver.find_element(*GapOrdersSearchLocators.SEARCH_TEXT_TEXTFIELD).send_keys(Keys.ENTER)

        def search_after_select(self, searchafterselect):
            """Method  to select from dropdown list

            returns:
                What we selected from dropdown
            """
            self.driver.find_element(*GapOrdersSearchLocators.SEARCH_AFTER_SELECTOR).send_keys(searchafterselect)
