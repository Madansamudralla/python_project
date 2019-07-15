# Created by petrisor.ureche at 7/9/2019
@all @api
Feature: getSubscription method scenarios
  # Call getSubscription method and get the response

#  @getSubscription @Digital
  Scenario Outline: Call getSubscription
    Given i have a "<subscription>" for a digital product
    When i make a getSubscription call on "<protocol>" with "<version>" and "<resource>"
    Then the http status code is 200
    And the RecurringEnabled equal true

    Examples:
      | protocol  | version | resource      | subscription |
      | rest      | 3.0     | subscriptions | 85419FDC8C   |
      | rest      | 4.0     | subscriptions | 85419FDC8C   |
      | rest      | 5.0     | subscriptions | 85419FDC8C   |
      | rest      | 6.0     | subscriptions | 85419FDC8C   |