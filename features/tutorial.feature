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

    Scenario: Quiz increases correct count on correct answer
      Given A quiz program
      And There is one question
      And Answer 1 is correct
      When The user answers 1
      And The program is run
      Then The result should be 1 of 1 questions correct

    Scenario: Nytt bättre quiz
      Given A quiz program
      And a question "Vad är meningen med livet, unversum och allting"
        | answer | correct |
        | 42     | True    |
        | 12     | False   |
      When The user answers 1
      And The program is run
      Then The result should be You answered 1 of 1 correct!

    @quiz
    Scenario: Ännu bättre hantering av frågor
      Given A quiz program
      And question with
        | prompt                                          | times_asked | times_correct | answer | correct |
        | Vad är meningen med livet universum och allting | 2           | 1             |        |         |
        |                                                 |             |               | 42     | True    |
        |                                                 |             |               | 12     | False   |
        |                                                 |             |               | 99     | False   |
      When The user answers 1
      And The program is run
      Then The result should be You answered 1 of 1 correct!

    @quiz
    Scenario: Svara fel på en fråga skall ge 0 av 1 rätt
      Given A quiz program
      And question with
        | prompt                                          | times_asked | times_correct | answer | correct |
        | Vad är meningen med livet universum och allting | 2           | 1             |        |         |
        |                                                 |             |               | 42     | True    |
        |                                                 |             |               | 12     | False   |
        |                                                 |             |               | 99     | False   |
      When The user answers 2
      And The program is run
      Then The result should be You answered 0 of 1 correct!