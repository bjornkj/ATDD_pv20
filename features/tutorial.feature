Feature: showing off behave
    Scenario Outline: Blend apple
      Given I put <thing> in a blender
      When I switch the blender on
      Then it should transform into <resulting thing>

    Examples: Thing to mix
      | thing   | resulting thing |
      | oranges | orange juice    |
      | apples  | apple juice     |

      Scenario: Mark all todos done
        Given I am on the todo page
        When I click done on all todos
        Then Remaining todos should be 0