from behave import given, when, then


@given('Open Sign-In page')
def open_page(context):
    context.app.sign_in_page.open_page()
    

@when('Locate Amazon logo')
def verify_the_page(context):
    pass


@when('Locate the email field')
def locate_email_field(context):
    pass


@when('Locate continue button')
def locate_continue_button(context):
    pass


@when('Locate Conditions of Use link')
def locate_conditions_link(context):
    pass


@when('Locate Privacy Notice link')
def locate_privacy_link(context):
    pass


@when('Locate Need help link')
def locate_help_link(context):
    pass


@when('Locate Forgot your password link')
def locate_forgot_password_link(context):
    pass


@when('Locate Other Issues link')
def locate_other_issues_link(context):
    pass