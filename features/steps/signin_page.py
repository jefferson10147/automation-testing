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
