from decouple import config
from selenium import webdriver

from app.application import Application


CHROME_DRIVER_PATH = config('CHROME_DRIVER_PATH')


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    context.app = Application(context.driver)
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
