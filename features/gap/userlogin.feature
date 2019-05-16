
Feature: Vendor Control Panel admin flows
  As an admin
  I want to be able to edit user access
  In order to prevent unauthorized access to the Cpanel

  @fixture.browser
  Scenario: Activate Cpanel users
    Given I am a Vendor Control Panel admin user
    When I login in the Vendor Control Panel