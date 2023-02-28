Feature: Login to Serenity Demo
  As a user
  In order to access my account
  I want to be able to login to the Serenity Demo website

  Scenario: Login with valid credentials
    Given I am on the Serenity Demo login page
    When I enter my username as "admin" and my password as "serenity"
    And I click the sign in button
    Then I should be redirected to the dashboard page
    And the page title should be "Dashboard - StartSharp"
    And I should see the text "Dashboard" in the h1 element

