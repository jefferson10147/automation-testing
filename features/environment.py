from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome('./chromedriver.exe')
    context.browser.maximize_window()
    context.browser.implicitly_wait(5)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.browser.delete_all_cookies()
    context.browser.quit()
