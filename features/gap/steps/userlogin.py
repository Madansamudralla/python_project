from behave import *
from features.gap.pages.login.login import LoginTest
import conf

use_step_matcher("re")


@given("I am a Vendor Control Panel admin user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@when("I login in the Vendor Control Panel")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logintest = LoginTest(context)
    logintest.login(conf.Username, conf.Password)
