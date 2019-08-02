# Created by alex.stoian at 1/8/2019
@all @api
Feature: setProductStatus method scenarios

  # Rest
  Scenario Outline: Call setProductStatus enable for a digital enabled product on rest
    Given i have an enabled digital product
    When i make a setProductStatus enable call on rest with "<version>" and "<resource>"
    Then the product is already "<status>" error should be thrown

    Examples:
      | version | resource | status  |
      | 3.0     | products | enabled |
      | 4.0     | products | enabled |
      | 5.0     | products | enabled |
      | 6.0     | products | enabled |

  # Rest
  Scenario Outline: Call setProductStatus enable for a digital disabled product on rest
    Given i have a disabled digital product
    When i make a setProductStatus enable call on rest with "<version>" and "<resource>"
    Then the http status code is 200
    And the response content is true
    And we revert the product status to disabled in the db

    Examples:
      | version | resource |
      | 3.0     | products |
      | 4.0     | products |
      | 5.0     | products |
      | 6.0     | products |

  # Rest
  Scenario Outline: Call setProductStatus disable for a digital disabled product on rest
    Given i have a disabled digital product
    When i make a setProductStatus disable call on rest with "<version>" and "<resource>"
    Then the product is already "<status>" error should be thrown

    Examples:
      | version | resource | status   |
      | 3.0     | products | disabled |
      | 4.0     | products | disabled |
      | 5.0     | products | disabled |
      | 6.0     | products | disabled |

 # Rest
  Scenario Outline: Call setProductStatus disable for a digital enabled product on rest
    Given i have an enabled digital product
    When i make a setProductStatus disable call on rest with "<version>" and "<resource>"
    Then the http status code is 200
    And the response content is true
    And we revert the product status to enabled in the db

    Examples:
      | version | resource |
      | 3.0     | products |
      | 4.0     | products |
      | 5.0     | products |
      | 6.0     | products |

  # Rpc
  Scenario Outline: Call setProductStatus enable for a digital enabled product on rpc
    Given i have an enabled digital product
    When i make a setProductStatus enable call on rpc version "<version>"
    Then the product is already "<status>" error should be thrown

    Examples:
      | version | status  |
      | 3.0     | enabled |
      | 4.0     | enabled |
      | 5.0     | enabled |
      | 6.0     | enabled |

  # Rpc
  Scenario Outline: Call setProductStatus enable for a digital disabled product on rpc
    Given i have a disabled digital product
    When i make a setProductStatus enable call on rpc version "<version>"
    Then the http status code is 200
    And the response content is true
    And we revert the product status to disabled in the db

    Examples:
      | version |
      | 3.0     |
      | 4.0     |
      | 5.0     |
      | 6.0     |

  # Rpc
  Scenario Outline: Call setProductStatus disable for a digital disabled product on rpc
    Given i have a disabled digital product
    When i make a setProductStatus disable call on rpc version "<version>"
    Then the product is already "<status>" error should be thrown

    Examples:
      | version | status   |
      | 3.0     | disabled |
      | 4.0     | disabled |
      | 5.0     | disabled |
      | 6.0     | disabled |

  # Rpc
  Scenario Outline: Call setProductStatus disable for a digital enabled product on rpc
    Given i have an enabled digital product
    When i make a setProductStatus disable call on rpc version "<version>"
    Then the http status code is 200
    And the response content is true
    And we revert the product status to enabled in the db

    Examples:
      | version |
      | 3.0     |
      | 4.0     |
      | 5.0     |
      | 6.0     |