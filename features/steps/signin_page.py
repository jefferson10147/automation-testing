from behave import given, when, then


@given('Open Sign-In page')
def open_page(context):
    context.app.sign_in_page.open_page()
    

@when('Locate Amazon logo')
def locate_logo(context):
    context.app.sign_in_page.locate_amazon_logo()


@when('Locate the email field')
def locate_email_field(context):
    context.app.sign_in_page.locate_email_field()


@when('Locate continue button')
def locate_continue_button(context):
    context.app.sign_in_page.locate_continue_btn()


@when('Locate Conditions of Use link')
def locate_conditions_link(context):
    context.app.sign_in_page.locate_conditions_link()


@when('Locate Privacy Notice link')
def locate_privacy_link(context):
    context.app.sign_in_page.locate_privacy_notice_link()


@when('Locate Need help link')
def locate_help_link(context):
    context.app.sign_in_page.locate_need_help_link()


@when('Locate Forgot your password link')
def locate_forgot_password_link(context):
    pass


@when('Locate Other Issues link')
def locate_other_issues_link(context):
    pass


@then('Locate Create your Amazon account button')
def locate_create_account_button(context):
    context.app.sign_in_page.locate_create_account_btn()
