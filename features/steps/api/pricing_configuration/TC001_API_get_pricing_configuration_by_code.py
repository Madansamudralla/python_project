import json

from behave import *

from features.api.pricing_configuration.get_pricing_configuration_by_code import GetPricingConfigurationByCode
from features.steps.api.assertions import assert_valid_schema

use_step_matcher("re")


@given("i have a digital product with a valid pricing configuration code")
def step_impl(context):
    context.pc_class = GetPricingConfigurationByCode(host=context.current_config['base_url'])
    context.product = context.pc_class.DIGITAL_PRODUCT
    context.pc_code = context.pc_class.PRICING_CONFIGURATION_CODE


@when('i make a getPricingConfigurationByCode call on rest with "(.*)" and "(.*)"')
def step_impl(context, version, resource):
    context.rest_response = context.pc_class.get_pricing_configuration_by_code_rest(
        version, resource, context.product, context.pc_code
    )


@step("the response body should be according with the schema")
def step_impl(context):
    if hasattr(context, 'rest_response'):
        response = json.loads(context.rest_response.content)
        assert_valid_schema(response, 'get_pricing_configuration_by_code_schema.json')
    elif hasattr(context, 'rpc_response'):
        response = json.loads(context.rpc_response.content)
        assert_valid_schema(response['result'], 'get_pricing_configuration_by_code_schema.json')


@when('i make a getPricingConfigurationByCode call on rpc on version "(.*)"')
def step_impl(context, version):
    context.rpc_response = context.pc_class.get_pricing_configuration_by_code_rpc(
        version, context.product, context.pc_code
    )
