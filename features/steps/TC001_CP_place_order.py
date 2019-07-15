from behave import use_step_matcher, given, step, when, then
from features.convert_plus.page_model.buy_link import BuyLinkThroughApi
from features.convert_plus.page_model.checkout_page import CheckoutPage

use_step_matcher("re")


@given('i am in the ConvertPlus "(.*)" checkout page with one digital product')
def step_impl(context, template):
    """
    :param template:
    :type template: str
    :type context: behave.runner.Context
    """
    get_base_url = BuyLinkThroughApi(host=context.current_config['api_cart_url'])
    get_base_url.get_on_base_url_catalog_digital_product(template)


@given('i am in the ConvertPlus "(.*)" checkout page with one physical product')
def step_impl(context, template):
    """
    :param template:
    :type template: str
    :type context: behave.runner.Context
    """
    get_base_url = BuyLinkThroughApi(host=context.current_config['api_cart_url'])
    get_base_url.get_on_base_url_catalog_physical_product(template)


@step("i wait for checkout page to load")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    wait = CheckoutPage()
    wait.wait_for_checkout_page_to_load()


@when('i fill the billing details for "(.*)" product')
def step_impl(context, type):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.fill_billing_details(
        'Netherlands', 'automation-3@avangate.com', type,
        'Dimitrie Pompei 10A', 'Bucharest', '020337', '0723654321')



@step("i fill the credit card details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.fill_cc_details('4111 1111 1111 1111', '12/22', '123')


@step("i fill the direct debit details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.fill_direct_debit_details('John Doe', 'NL28RBOS0440339464', 'RBOSNL2A')


@step("i fill the wire transfer details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.fill_wire_transfer_details('John Doe')


@step("i click on Place order button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.click_on_place_order()


@step("i select Direct Debit as a payment method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.select_direct_debit_as_a_payment_method()


@step("i select Wire Transfer as a payment method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.select_wire_transfer_as_a_payment_method()


@step("i select PayPal as a payment method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.select_paypal_as_a_payment_method()


@then("the finish page is fully loaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    checkout = CheckoutPage()
    checkout.the_finish_page_is_fully_loaded()


@step("i am redirected to PayPal from cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
