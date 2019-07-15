# Created by petrisor.ureche at 5/29/2019
@all @convert_plus
Feature: Convert Plus Default and One-Column scenarios
  # Place orders on default and one-column templates.

#  @CC @Digital
  Scenario Outline: Place order with one digital product on default and one-column templates.
    Given i am in the ConvertPlus "<template>" checkout page with one digital product
    And i wait for checkout page to load
    When i fill the billing details for "<type>" product
    And i fill the credit card details
    And i click on Place order button
    Then the finish page is fully loaded

    Examples:
      | template   | type     |
      | default    | digital  |
      | one-column | digital  |

#  @DirectDebit @Digital
  Scenario Outline: Place order with one digital product on default and one-column templates.
    Given i am in the ConvertPlus "<template>" checkout page with one digital product
    And i wait for checkout page to load
    When i fill the billing details for "<type>" product
    And i select Direct Debit as a payment method
    And i fill the direct debit details
    And i click on Place order button
    Then the finish page is fully loaded

    Examples:
      | template   | type     |
      | default    | digital  |
      | one-column | digital  |

#  @WireTransfer @Digital
  Scenario Outline: Place order with one digital product on default and one-column templates.
    Given i am in the ConvertPlus "<template>" checkout page with one digital product
    And i wait for checkout page to load
    When i fill the billing details for "<type>" product
    And i select Wire Transfer as a payment method
    And i fill the wire transfer details
    And i click on Place order button
    Then the finish page is fully loaded

    Examples:
      | template   | type     |
      | default    | digital  |
      | one-column | digital  |

#  @PayPal @Digital
#  Scenario Outline: Place order with one digital product on default and one-column templates.
#    Given i am in the ConvertPlus "<template>" checkout page with one digital product
#    And i wait for checkout page to load
#    When i fill the billing details for "<type>" product
#    And i select PayPal as a payment method
#    And i am redirected to PayPal from cart
##    And i fill the wire transfer details
##    And i click on Place order button
##    Then the finish page is fully loaded

    Examples:
      | template   | type     |
      | default    | digital  |
      | one-column | digital  |


#  @CC @Physical
  Scenario Outline: Place order with one physical product on default and one-column templates.
    Given i am in the ConvertPlus "<template>" checkout page with one physical product
    And i wait for checkout page to load
    When i fill the billing details for "<type>" product
    And i fill the credit card details
    And i click on Place order button
    Then the finish page is fully loaded

    Examples:
      | template   | type     |
      | default    | physical |
      | one-column | physical |

#  @DirectDebit @Physical
  Scenario Outline: Place order with one physical product on default and one-column templates.
    Given i am in the ConvertPlus "<template>" checkout page with one physical product
    And i wait for checkout page to load
    When i fill the billing details for "<type>" product
    And i select Direct Debit as a payment method
    And i fill the direct debit details
    And i click on Place order button
    Then the finish page is fully loaded

    Examples:
      | template   | type     |
      | default    | physical |
      | one-column | physical |

#  @WireTransfer @Physical
  Scenario Outline: Place order with one digital product on default and one-column templates.
    Given i am in the ConvertPlus "<template>" checkout page with one physical product
    And i wait for checkout page to load
    When i fill the billing details for "<type>" product
    And i select Wire Transfer as a payment method
    And i fill the wire transfer details
    And i click on Place order button
    Then the finish page is fully loaded

    Examples:
      | template   | type       |
      | default    | physical   |
      | one-column | physical   |