import json

from behave import use_step_matcher, given, step, when, then
from features.api.subscription.get_subscription import GetSubscription

use_step_matcher("re")


@given('i have a "(.*)" for a digital product')
def step_impl(context, subscription):
    """
    :type context: behave.runner.Context
    :type status: str
    """
    call = GetSubscription(host=context.current_config['base_url'])
    context.subscription = call.get_subscription_reference(subscription)


@when('i make a getSubscription call on "(.*)" with "(.*)" and "(.*)"')
def step_impl(context, protocol, version, resource):
    """
    :type context: behave.runner.Context
    :type protocol: str
    :type version: str
    :type resource: str
    """
    call = GetSubscription(host=context.current_config['base_url'])
    context.response = call.call_get_subscription(protocol, version, resource)


@step("the RecurringEnabled equal true")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = json.loads(context.response.content)
    assert response['RecurringEnabled'] is True
