from behave import given, when, then


@given('Open Amazon page')
def open_main_page(context):
    context.app.main_page.open_amazon_main_page()


@when('Click in cart icon')
def click_in_icon(context):
    context.app.main_page.click_in_cart_icon()


@then('Verify the cart is empty')
def verify_cart(context):
    context.app.main_page.verify_empty_cart_text()
