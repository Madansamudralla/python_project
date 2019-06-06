from behave import *
from features.convert_plus.page_model.buy_link_through_api import BuyLinkThroughApi
from features.convert_plus.page_model.checkout_page import CheckoutPage

use_step_matcher("re")


@given('I am in the ConvertPlus default "(.*)" checkout page with one regular product')
def step_impl(context, template):
    """
    :param template:
    :type template: str
    :type context: behave.runner.Context
    """
    get_base_url = BuyLinkThroughApi()
    get_base_url.get_on_base_url(template)

@step("I wait for checkout page to load")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    wait = CheckoutPage()
    wait.wait_for_checkout_page_to_load()


@when("I fill the billing details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.fill_country('Netherlands')
    checkout.wait_for_loader_to_disappear()


@step("I fill the credit card details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.fill_email_address('cp_behave@2checkout.com')
    checkout.fill_cc_details('4111 1111 1111 1111', '12/22', '123')


@step("I click on Place order button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.click_on_place_order()


@then("the finish page is fully loaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.the_finish_page_is_fully_loaded()
