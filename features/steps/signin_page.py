from behave import given, when, then


@given('Open Sign-In page')
def open_page(context):
    context.app.sign_in_page.open_page()
    

@when('Verify the correct page is openned')
def verify_the_page(context):
    pass
