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
    call.get_product_status_db(call.DIGITAL_PRODUCT, status)


@when('i make a getProductByCode call on rest with "(.*)" and "(.*)"')
def step_impl(context, version, resource):
    """
    :type context: behave.runner.Context
    :type version: str
    :type resource: str
    """
    call = GetProductByCode(host=context.current_config['base_url'])
    context.rest_response = call.get_product_by_code_rest(version, resource)


@when('i make a getProductByCode call on rpc on version "(.*)"')
def step_impl(context, version):
    """
    :type context: behave.runner.Context
    :type version: str
    """
    call = GetProductByCode(host=context.current_config['base_url'])
    context.rpc_response = call.get_product_by_code_rpc(version)


@then("the http status code is 200")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, 'rest_response'):
        assert context.rest_response.status_code == 200, f"Expected: 200, Actual: {context.rest_response.status_code}"
    elif hasattr(context, 'rpc_response'):
        assert context.rpc_response.status_code == 200, f"Expected: 200, Actual: {context.rest_response.status_code}"
