from behave import given, when, then


@given('Open Amazon help page')
def open_help_page(context):
    context.app.help_page.open_page()


@when('Search for cancel order')
def search_in_searchbar(context):
    context.app.help_page.search_for_cancel_orders()


@then('Verify Cancel Items or Orders text is present')
def verify_text_is_present(context):
    context.app.help_page.verify_cancel_order_text()
