@sanity
Feature: Search feature

  Background:
    Given I navigate to google.com

  Scenario: Validating the search feature
    When I validate the page title
    Then I enter the text as "Hello Selenium"
    And I click the search button

  Scenario: Validating the search feature with new text
    When I validate the page title
    Then I enter the text as "Hello Behave"
    And I click the search button