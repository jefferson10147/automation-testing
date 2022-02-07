from behave import given, when, then


@given('Open Amazon help customer page')
def open_page(context):
    context.app.help_customer_page.open_help_page()


@when('Locate the title')
def locate_title(context):
    context.app.help_customer_page.locate_welcome_text()


@when('Locate cards')
def locate_cards(context):
    context.app.help_customer_page.locate_cards()


@when('Locate search bar')
def locate_bar(context):
    context.app.help_customer_page.locate_search_bar()


@when('Locate topics title')
def locate_title(context):
    context.app.help_customer_page.locate_topics_title()


@then('Locate topics')
def locate_topics(context):
    context.app.help_customer_page.locate_topics()
