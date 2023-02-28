Feature: Registration Feature
  Scenario Outline: Validating the Registration Feature
    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    Then I enter the phone number as "<Phone number>"
    And I enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click on the submit button
    Examples:
      | name        | Phone number | email                      | country | city   | username       | password |
      | Rahul Arora | 9711111558   | trainer@way2automation.com | India   | Delhi  | rahularora1985 | asdfsdfdf|
      | Raman Arora | 9711911558   | java@way2automation.com    | Germany | Berlin | ramanarora1986 | werwerwer|