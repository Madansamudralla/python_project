# Created by petrisor.ureche at 5/29/2019
@all @convert_plus
Feature: Convert Plus Default and One-Column scenarios
  # Place orders on default and one-column templates.

  Scenario Outline: Place order on default and one-column templates.
    Given I am in the ConvertPlus default "<template>" checkout page with one regular product
    And I wait for checkout page to load
    When I fill the billing details
    And I fill the credit card details
    And I click on Place order button
    Then the finish page is fully loaded

  Examples:
      | template   |
      | default    |
      | one-column |