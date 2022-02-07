Feature: test cases for product page

    Scenario: User can add a product to cart
        Given Open Amazon page
        When Search in the search field for PS4 controller
        And Click in first product
        And Add product to the cart
        Then Verify there are 1 products added in the cart