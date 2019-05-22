Feature: Search in Wikipedia
  As a guest, I want to be able to search for articles on Wikipedia

  Scenario: Search for "notre dame"
    Given I am on the Wikipedia homepage
      """
      https://en.wikipedia.org/
      """
    When I search for "notre dame"
    And I click on Notre-Dame de Paris
    Then I should be on Notre Dame de Paris page

  @wip
  Scenario: Search for "notre dame"
    Given I am on the Wikipedia homepage
      """
      https://en.wikipedia.org/
      """
    When I search for <search_text> string
     | search_text |
     | notre dame  |
    And I click on Notre-Dame de Paris
    Then I should be on Notre Dame de Paris page
