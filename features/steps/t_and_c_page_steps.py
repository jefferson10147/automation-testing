from behave import given, when, then


@given('Open Amazon T&C page')
def open_page(context):
    context.app.t_and_c_page.open_page()


@when('Store original windows')
def store_window(context):
    context.app.t_and_c_page.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_link(context):
    context.app.t_and_c_page.click_in_privacy_link()


@when('Switch to the newly opened window')
def switch_windo(context):
    context.app.t_and_c_page.switch_to_new_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_link(context):
    context.app.t_and_c_page.verify_private_page_is_open()


@then('User can close new window and switch back to original')
def switch_to_original(context):
    context.app.t_and_c_page.switch_to_original_page()
