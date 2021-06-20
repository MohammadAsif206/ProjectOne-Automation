Feature: employee add a request

  Background: login as an employee
    Given The Guest is on the login Home Page
    When The Guest types Mohammad into the username bar
    When The Guest types Asif into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say Welcome to employee
    When The guest clicks ok on alert prompt
    Then The guest should be on employee page



  Scenario Outline: adding a request
    When The Guest types <amount> into the amount bar
    When The Guest types <reason> into the reason bar
    When The Guest types <status> into the status bar
    When The Guest clicks on the submit button
    Then The prompt alert text should be <text>
    When The guest clicks ok on alert prompt


    Examples:
      | amount | reason | status | text |
      | 1000 | travel | pending | The request was successfully submitted |



   Scenario Outline: adding a request with an empty field
     When The Guest types <amount> into the amount bar
     When The Guest types <reason> into the reason bar
     When The Guest clicks on the submit button
     Then The prompt alert text should be <text>
     When The guest clicks ok on alert prompt

     Examples:
      | amount | reason | text |
      | 900 | approved | some fields are empty |


    Scenario Outline: adding a request with wrong value type for amount
      When The Guest types <amount> into the amount bar
      When The Guest types <reason> into the reason bar
      When The Guest types <status> into the status bar
      When The Guest clicks on the submit button
      Then The prompt alert text should be <text>
      When The guest clicks ok on alert prompt


      Examples:
        | amount | reason | status | text |
        | a | travel | pending | some fields are empty |




