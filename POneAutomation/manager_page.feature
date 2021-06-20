Feature: manager update a request

  Background: login as a manager
    Given The Guest is on the login Home Page
    When The Guest types Olive into the username bar
    When The Guest types Oil into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and and say Welcome to manager
    When The guest clicks ok on alert prompt
    Then The guest should be on manager page



  Scenario Outline: updating a request

    When The Guest types <id> into the id bar
    When The Guest types <status> into the request status bar
    When The Guest types <comment> into the request comment bar
    When The Guest clicks on the request submit button
    Then The prompt alert text should be <text>
    When The guest clicks ok on alert prompt


    Examples:
      | id | status | comment | text |
      | 1 | pending | good | The request was successfully updated |
      | 12255 | accepted | bad | The resource was not found |
      | 2 | rejected | bad | The request was successfully updated |
      | 0 | pending | bad | The resource was not found |

        Scenario Outline: updating a request with an empty field

    When The Guest types <id> into the id bar
    When The Guest clicks on the request submit button
    Then The prompt alert text should be <text>
    When The guest clicks ok on alert prompt


    Examples:
      | id | text |
      | 32 | some fields are empty |
