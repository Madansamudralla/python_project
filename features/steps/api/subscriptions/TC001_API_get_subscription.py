import json

from behave import use_step_matcher, given, step, when, then
from features.api.subscription.get_subscription import GetSubscription

use_step_matcher("re")


@given('i have a "(.*)" for a digital product')
def step_impl(context, subscription):
    """
    :type context: behave.runner.Context
    :type subscription: str
    """
    call = GetSubscription(host=context.current_config['base_url'])
    context.subscription = call.get_subscription_reference(subscription)


@when('i make a getSubscription call on rest with "(.*)" and "(.*)"')
def step_impl(context, version, resource):
    """
    :type context: behave.runner.Context
    :type version: str
    :type resource: str
    """
    call = GetSubscription(host=context.current_config['base_url'])
    context.rest_response = call.call_get_subscription_rest(version, resource)


@when('i make a getSubscription call on rpc on version "(.*)"')
def step_impl(context, version):
    """
    :type context: behave.runner.Context
    :type version: str
    """
    call = GetSubscription(host=context.current_config['base_url'])
    context.rpc_response = call.call_get_subscription_rpc(version)


@step("the RecurringEnabled equals true")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, 'rest_response'):
        response = json.loads(context.rest_response.content)
    elif hasattr(context, 'rpc_response'):
        response = json.loads(context.rpc_response.content)['result']
    else:
        raise Exception("The response has not been correctly fetched.")

    assert response['RecurringEnabled'] is True
