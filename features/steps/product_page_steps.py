from behave import given, when, then


@given('Open product page with id {product_id}')
def open_page(context, product_id):
    context.app.product_page.open_product_page(product_id)


@given('Open Wholefoods page')
def open_wholefood_page(context):
    context.app.product_page.open_wholefoods_page()


@when('Search in the search field for {product}')
def search_product(context, product):
    context.app.nav_bar.input_into_search_bar(text=product)


@when('Click in first product')
def click_product(context):
    context.app.product_page.click_in_first_product()


@when('Add product to the cart')
def add_product(context):
    context.app.product_page.add_to_cart()


@when('Click in close button')
def click_btn(context):
    context.app.product_page.click_close_btn()


@then('Verify there are {number_of_items} products added in the cart')
def verify_number(context, number_of_items):
    context.app.nav_bar.verify_cart_count(number_of_items)


@then('User can click over all colors')
def verify_colors(context):
    context.app.product_page.verify_colors()


@then('Verify the regular word')
def verify_word(context):
    context.app.product_page.verfiy_regular_text()
