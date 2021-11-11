@things.req.browser
Feature: showing off behave
    @blender
    Scenario Outline: Blend apple
      Given I put <thing> in a blender
      When I switch the blender on
      Then it should transform into <resulting thing>
    Examples: Thing to mix
      | thing   | resulting thing |
      | oranges | orange juice    |
      | apples  | apple juice     |
    @web
    Scenario: Mark all todos done
      Given I am on the todo page
      When I click done on all todos
      Then Remaining todos should be 0
    @quiz
    Scenario: Quiz increases correct count on correct answer
      Given A quiz program
      And There is one question
      And Answer 1 is correct
      When The user answers 1
      And The program is run
      Then The result should be 1 of 1 questions correct