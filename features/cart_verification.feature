Feature: Cart verification

Background:
  Given that a User is opened nopCommerce app and a user is positioned on the home page

  @blocker
  Scenario: User wants to add electronics item into cart
    When a user selects Camera & photo option from the Electronics menu
    And a user clicks on the Add to cart option on the first item
    Then the message that product is added is shown
    And the product is shown in the Shopping cart

  Scenario: User wants to add more products
    When a user selects Camera & photo option from the Electronics menu
    And a user adds two same items into cart
    Then the quantity value in the cart for the added product is set to 2

  @critical
  Scenario: User wants to delete product from the cart
    When a user selects Camera & photo option from the Electronics menu
    And a user clicks on the Add to cart option on the first item
    And user opens the Cart page
    And user click on the remove button
    Then the product is deleted and appropriate message is shown

  Scenario: User wants to search for a product
    When User inputs value in the search field
    And user click on the search field
    Then searched products are shown





