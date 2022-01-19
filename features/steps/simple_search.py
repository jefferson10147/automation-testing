from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open python page')
def open_main_page(context):
    context.driver.get('http://www.python.org')


@when('Verify the correct page is openned')
def verify_python_page(context):
    assert 'Python' in context.driver.title


@when('Search for Pycon in the search bar')
def search_in_search_bar(context):
    elem = context.driver.find_element(By.ID, 'id-search-field')
    elem.clear()
    elem.send_keys('pycon')
    elem.send_keys(Keys.RETURN)


@then('Verify there are not results')
def verify_no_results(context):
    assert 'No results found.' not in context.driver.page_source
    # sleep(5)
