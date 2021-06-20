Feature:login
  Background:login Home Page
    Given The Guest is on the login Home Page

  Scenario: login as an employee
    When The Guest types Mohammad into the username bar
    When The Guest types Asif into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say Welcome to employee
    When The guest clicks ok on alert prompt
    Then The guest should be on employee page


  Scenario:login as a manager
    When The Guest types Olive into the username bar
    When The Guest types Oil into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and and say Welcome to manager
    When The guest clicks ok on alert prompt
    Then The guest should be on manager page

  Scenario:login with wrong credential
    When The Guest types Cold into the username bar
    When The Guest types Winter into the password bar
    When The Guest clicks on the signin button
    Then The alert prompts and say Either entered username or password is wrong.
    When The guest clicks ok on alert prompt



