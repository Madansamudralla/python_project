# Created by petrisor.ureche at 7/5/2019
@all @api
Feature: getProductByCode method scenarios
  # Call getProductByCode method and get the response

#  @getProductByCode @Digital
  Scenario Outline: Call getProductByCode
    Given i have a digital product with "<status>"
    When i make a getProductByCode call on "<protocol>" with "<version>" and "<resource>"
    Then the http status code is 200

    Examples:
      | protocol  | version | resource | status    |
      | rest      | 3.0     | products | enabled   |
      | rest      | 4.0     | products | enabled   |
      | rest      | 5.0     | products | enabled   |
      | rest      | 6.0     | products | enabled   |