# Created by petrisor.ureche at 7/9/2019
@all @api
Feature: getSubscription method scenarios
  # Call getSubscription method and get the response

#  @getSubscription @Digital
  Scenario Outline: Call getSubscription for a digital product on rest
    Given i have a "<subscription>" for a digital product
    When i make a getSubscription call on rest with "<version>" and "<resource>"
    Then the http status code is 200
    And the RecurringEnabled equals true

    Examples:
      | version | resource      | subscription |
      | 3.0     | subscriptions | 85419FDC8C   |
      | 4.0     | subscriptions | 85419FDC8C   |
      | 5.0     | subscriptions | 85419FDC8C   |
      | 6.0     | subscriptions | 85419FDC8C   |

  Scenario Outline: Call getSubscription for a digital product on rpc
    Given i have a "<subscription>" for a digital product
    When i make a getSubscription call on rpc on version "<version>"
    Then the http status code is 200
    And the RecurringEnabled equals true

    Examples:
      | version | subscription |
      | 3.0     | 85419FDC8C   |
      | 4.0     | 85419FDC8C   |
      | 5.0     | 85419FDC8C   |
      | 6.0     | 85419FDC8C   |