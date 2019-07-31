from core.common.cpanel.locators.setup.products_page_loc import ProductsPageLocators, AddProductPageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import core


class CpanelProducts:

    def __init__(self):
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def add_product(self):
        self.driver.find_element(*ProductsPageLocators.ADD_NEW_PRODUCT).click()

    def search_product_name(self, prodname):
        self.driver.find_element(*ProductsPageLocators.PRODUCT_NAME).sendkeys(prodname)

    def search_prod_type(self, value):
        Select(self.driver.find_element(*ProductsPageLocators.PRODUCT_TYPE)).select_by_value(value)


class CpanelAddProduct(CpanelProducts):

    def set_product_name(self, name='FrameworkCreatedProduct'):
        self.driver.find_element(*AddProductPageLocators.ADD_PRODUCT_NAME).send_keys(name)

    def set_version(self, version=""):
        self.driver.find_element(*AddProductPageLocators.VERSION_MODEL).send_keys(version)

    def set_product_group(self, groupname='General'):
        Select(self.driver.find_element(*AddProductPageLocators.PRODUCT_GROUP)).select_by_visible_text(groupname)

    def set_external_reference(self, refname=""):
        self.driver.find_element(*AddProductPageLocators.EXTERNAL_REFERENCE).send_keys(refname)

    def set_quantity(self, status='1'):
        radio_btn = self.driver.find_element(*AddProductPageLocators.QUANTITY)
        if status == '0' and radio_btn.is_selected():
            radio_btn.click()

    def set_product_type_regular(self, option='1'):
        if option == 0:
            self.driver.find_element(*AddProductPageLocators.PRODUCT_TYPE_BUNDLE).click()

    def set_currency(self, currency='USD'):
        Select(self.driver.find_element(*AddProductPageLocators.DEFAULT_CURRENCY)).select_by_visible_text(currency)

    def set_base_price(self, status='0'):
        radio_btn = self.driver.find_element(*AddProductPageLocators.HAS_BASE_PRICE)
        if status == '1' and not radio_btn.is_selected():
            radio_btn.click()

    def set_price_value(self, value='60'):
        self.driver.find_element(*AddProductPageLocators.PRICE).send_keys(value)

    def set_billing_cycle(self, value='one time fee'):
        # other values: MONTHS, DAYS
        Select(self.driver.find_element(*AddProductPageLocators.BILLING_CYCLE)).select_by_visible_text(value)

    def set_cycle_duration(self, amount):
        self.driver.find_element(*AddProductPageLocators.BILLING_CYCLE_UNITS).send_keys(amount)

    # def set_short_description(self, desc=''):
    #     # BROKEN. look up workarounds for iframes
    #     self.driver.switch_to.frame(0)
    #     self.driver.find_element(*AddProductPageLocators.SHORT_DESC).sendkeys(desc)
    #
    # def set_long_description(self, desc=''):
    #     # BROKEN. look up workarounds for iframes
    #     self.driver.find_element(*AddProductPageLocators.LONG_DESC).send_keys(desc)

    def set_categories(self, category='Select category'):
        Select(self.driver.find_element(*AddProductPageLocators.CATEGORY)).select_by_visible_text(category)

    # work in progress
    # def set_platforms(self, *args):
    #     if args in AddProductPageLocators.platforms:
    #         item = self.driver.find_element(AddProductPageLocators.platforms[args])
    #         if not item.is_selected():
    #             item.click()
    #     else:
    #         print(args + 'is not included in platform list')

    def save_product(self):
        self.driver.find_element(*AddProductPageLocators.ADD_PRODUCT_SAVE).click()
