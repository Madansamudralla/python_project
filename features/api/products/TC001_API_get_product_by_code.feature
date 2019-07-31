# Created by petrisor.ureche at 7/5/2019
@all @api
Feature: getProductByCode method scenarios

#  @getProductByCode @Digital
  Scenario Outline: Call getProductByCode for a digital product on rest
    Given i have a digital product with "<status>"
    When i make a getProductByCode call on rest with "<version>" and "<resource>"
    Then the http status code is 200

    Examples:
      | version | resource | status    |
      | 3.0     | products | enabled   |
      | 4.0     | products | enabled   |
      | 5.0     | products | enabled   |
      | 6.0     | products | enabled   |

  Scenario Outline: Call getProductByCode for a digital product on rpc
    Given i have a digital product with "<status>"
    When i make a getProductByCode call on rpc on version "<version>"
    Then the http status code is 200

    Examples:
      | version | status  |
      | 3.0     | enabled |
      | 4.0     | enabled |
      | 5.0     | enabled |
      | 6.0     | enabled |
