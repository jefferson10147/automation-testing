Feature: test cases for product page

    Scenario: User can add a product to cart
        Given Open Amazon page
        When Search in the search field for PS4 controller
        And Click in first product
        And Add product to the cart
        Then Verify there are 1 products added in the cart

    Scenario: User see all colors in certain product
        Given Open product page with id B07BJL37GD
        Then User can click over all colors

    Scenario: User can see word regular on wholefoods products
        Given Open Wholefoods page
        When Click in close button
        Then Verify the regular word

    Scenario: User can select a deparment and search for a product
        Given Open Amazon page
        When Click in deparments dropdown
        When Click in Videogames option
        And Search in the search field for ps4
        Then Verify "ps4" text is present in result page
