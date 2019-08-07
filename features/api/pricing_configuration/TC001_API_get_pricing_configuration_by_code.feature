# Created by alex.stoian at 2/8/2019
@all @api
Feature: getPricingConfigurationByCode method scenarios

  # Rest
  Scenario Outline: Call getPricingConfigurationByCode for a digital product on rest
    Given i have a digital product with a valid pricing configuration code
    When i make a getPricingConfigurationByCode call on rest with "<version>" and "<resource>"
    Then the http status code is 200
    And the response body should be according with the schema

    Examples:
      | version | resource |
      | 3.0     | products |
      | 4.0     | products |
      | 5.0     | products |
      | 6.0     | products |

  Scenario Outline: Call getPricingConfigurationByCode for a digital product on rpc
    Given i have a digital product with a valid pricing configuration code
    When i make a getPricingConfigurationByCode call on rpc on version "<version>"
    Then the http status code is 200
    And the response body should be according with the schema

    Examples:
      | version |
      | 3.0     |
      | 4.0     |
      | 5.0     |
      | 6.0     |