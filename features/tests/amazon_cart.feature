Feature: test cases for amazon cart

    Scenario: User verify cart is empty
        Given Open Amazon page
        When Click in cart icon
        Then Verify the cart is empty
