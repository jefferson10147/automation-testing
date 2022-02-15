from behave import given, then


@given('Open Amazon best sellers page')
def open_page(context):
    context.app.best_sellers.open_best_sellers_page()


@then('Verify there are {number_of_links} links')
def verify_links(context, number_of_links):
    context.app.best_sellers.locate_elements()
    context.app.best_sellers.verify_links(int(number_of_links))


@then('Verify links are clickable')
def click_links(context):
    context.app.best_sellers.click_in_links()
