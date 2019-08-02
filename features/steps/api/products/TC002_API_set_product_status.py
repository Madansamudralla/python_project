import json

from behave import use_step_matcher, given, step, when, then

from features.api.products.set_product_status import SetProductStatus

use_step_matcher("re")


@when('i make a setProductStatus enable call on rest with "(.*)" and "(.*)"')
def step_impl(context, version, resource):
    """
    :type context: behave.runner.Context
    :type version: str
    :type resource: str
    """
    context.rest_response = context.ps_class.set_product_status_enabled_rest(
        version, resource, context.product
    )


@then('the product is already "(.*)" error should be thrown')
def step_impl(context, status):
    if hasattr(context, 'rest_response'):
        response = json.loads(context.rest_response.content)
        assert response['error_code'] == "INVALID_PRODUCT_STATUS", \
            f"The error code is not as expected: {response['error_code']}"
        assert response['message'] == f"The product is already {status.upper()}", \
            f"The error message is not as expcetd: {response['message']}"
    elif hasattr(context, 'rpc_response'):
        response = json.loads(context.rpc_response.content)
        assert response['error']['message'] == f"INVALID_PRODUCT_STATUS: The product is already {status.upper()}", \
            f"The error message is not as expected: {response['error']['message']}"


@step("we revert the product status to disabled in the db")
def step_impl(context):
    context.ps_class.set_product_status_db(context.product, "disabled")


@given("i have a disabled digital product")
def step_impl(context):
    context.ps_class = SetProductStatus(host=context.current_config['base_url'])
    context.ps_class.get_product_status_db(context.ps_class.DISABLED_DIGITAL_PRODUCT, "disabled")
    context.product = context.ps_class.DISABLED_DIGITAL_PRODUCT


@given("i have an enabled digital product")
def step_impl(context):
    context.ps_class = SetProductStatus(host=context.current_config['base_url'])
    context.ps_class.get_product_status_db(context.ps_class.ENABLED_DIGITAL_PRODUCT, "enabled")
    context.product = context.ps_class.ENABLED_DIGITAL_PRODUCT


@when('i make a setProductStatus disable call on rest with "(.*)" and "(.*)"')
def step_impl(context, version, resource):
    """
    :type context: behave.runner.Context
    :type version: str
    :type resource: str
    """
    context.rest_response = context.ps_class.set_product_status_disabled_rest(
        version, resource, context.product
    )


@step("we revert the product status to enabled in the db")
def step_impl(context):
    context.ps_class.set_product_status_db(context.product, "enabled")


@step("the response content is true")
def step_impl(context):
    if hasattr(context, 'rest_response'):
        assert context.rest_response.content == b'true', \
            f"Expecting the response to be true, got: {context.rest_response.content}"
    elif hasattr(context, 'rpc_response'):
        response = json.loads(context.rpc_response.content)
        assert response['result'] is True, f"Expecting the response to be true, got: {response['result']}"


@when('i make a setProductStatus enable call on rpc version "(.*)"')
def step_impl(context, version):
    context.rpc_response = context.ps_class.set_product_status_rpc(version, context.product, True)


@when('i make a setProductStatus disable call on rpc version "(.*)"')
def step_impl(context, version):
    context.rpc_response = context.ps_class.set_product_status_rpc(version, context.product, False)
