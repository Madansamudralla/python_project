from behave import use_step_matcher, given, step, when, then
from features.api.products.get_product_by_code import GetProductByCode

use_step_matcher("re")


@given('i have a digital product with "(.*)"')
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    :type status: str
    """
    call = GetProductByCode(host=context.current_config['base_url'])
    call.see_product_status(status)


@when('i make a getProductByCode call on "(.*)" with "(.*)" and "(.*)"')
def step_impl(context, protocol, version, resource):
    """
    :type context: behave.runner.Context
    :type protocol: str
    :type version: str
    :type resource: str
    """
    call = GetProductByCode(host=context.current_config['base_url'])
    context.response = call.call_get_product_by_code(protocol, version, resource)


@then("the http status code is 200")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200

