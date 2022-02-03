Feature: test cases for help page

    Scenario: User can cancel orders
        Given Open Amazon help page
        When Search for cancel order
        Then Verify Cancel Items or Orders text is present
