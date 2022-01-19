Feature: Simple Search

    Scenario: User can make a simple search in Python page
        Given Open python page
        When Verify the correct page is openned
        And Search for Pycon in the search bar
        Then Verify there are not results
        