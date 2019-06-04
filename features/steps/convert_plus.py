from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from features.convert_plus.page_model.buy_link_through_api import ApiBuyLink
from features.convert_plus.locators.checkout_page import CheckoutPageLocators
from features.convert_plus.page_model.checkout_page import CheckoutPage
import time

use_step_matcher("re")


@given('I am in the ConvertPlus default "(.*)" checkout page with one regular product')
def step_impl(context, template):
    """
    :type context: behave.runner.Context
    """
    response = ApiBuyLink()
    if template == "default":
        url = response.buy_link_with_one_regular_product_on_default_template()
    elif template == "one-column":
        url = response.buy_link_with_one_regular_product_on_one_column_template()
    context.browser.get(url)


@step("I wait for checkout page to load")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    WebDriverWait(context.browser, 30).until(
        EC.visibility_of_element_located(CheckoutPageLocators.PLACE_ORDER_BUTTON_LOCATOR)
    )


@when("I fill the billing details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage(context.browser)
    checkout.fill_country('Netherlands')
    checkout.wait_for_loader_to_disappear()


@step("I fill the credit card details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage(context.browser)
    checkout.fill_email_address('cp_behave@2checkout.com')
    checkout.fill_cc_details('4111 1111 1111 1111', '12/22', '123')


@step("I click on Place order button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage(context.browser)
    checkout.click_on_place_order()


@then("the finish page is fully loaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage(context.browser)
    checkout.the_finish_page_is_fully_loaded()

