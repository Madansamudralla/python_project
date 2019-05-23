from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher("re")


@given("I am on the Wikipedia homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(context.text)


@when('I search for "(.*)"')
def step_impl(context, search_text):
    """
    :type context: behave.runner.Context
    :param search_text: str
    """
    search_input = context.driver.find_element_by_id("searchInput")
    search_input.send_keys(search_text)


@then("I should be on Notre Dame de Paris page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.current_url == 'https://en.wikipedia.org/wiki/Notre-Dame_de_Paris'
    assert context.driver.title == 'Notre-Dame de Paris - Wikipedia'


@step("I click on (.*)")
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    :param text: str
    """
    elements = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "mw-searchSuggest-link"))
    )
    for element in elements:
        if element.get_attribute('title') == text:
            element.click()
            break


@when("I search for <search_text> string")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    search_input = context.driver.find_element_by_id("searchInput")
    search_input.send_keys(context.table[0]['search_text'])
