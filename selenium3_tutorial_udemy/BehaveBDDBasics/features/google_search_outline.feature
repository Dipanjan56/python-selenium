@smoke
Feature: Search feature
  Scenario Outline: Validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text as "<searchTitle>"
    And I click the search button
    Examples:
      | searchTitle |
      | Hello BDD   |
      | Hello TDD   |
