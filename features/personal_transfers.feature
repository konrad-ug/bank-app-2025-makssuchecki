Feature: Personal transfers

Scenario: User receives an incoming transfer
    Given a personal account with pesel "89092909246" and balance of 100
    When an incoming transfer of 100 is credited to the account
    Then the account balance should be 200

Scenario: Transfer is rejected when incoming amount is negative
    Given a personal account with pesel "89092909246" and balance of 100
    When an incoming transfer of -100 is credited to the account
    Then the transfer should be rejected
    And the account balance should be 100

Scenario: User sends an outgoing transfer
    Given a personal account with pesel "89092909246" and balance of 100
    When an outgoing transfer of 50 is executed 
    Then the account balance should be 50

Scenario: Transfer is rejected when outgoing amount is negative
    Given a personal account with pesel "89092909246" and balance of 100
    When an outgoing transfer of -50 is executed 
    Then the transfer should be rejected
    And the account balance should be 100

Scenario: Transfer is rejected when the funds are insufficient
    Given a personal account with pesel "89092909246" and balance of 100
    When an outgoing transfer of 200 is executed 
    Then the transfer should be rejected
    And the account balance should be 100

Scenario: User sends a series of transfers
    Given a personal account with pesel "89092909246" and balance of 100
    When an incoming transfer of 100 is credited to the account
    And an incoming transfer of 200 is credited to the account
    And an outgoing transfer of 50 is executed
    Then the account balance should be 350 

