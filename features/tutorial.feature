Feature: showing off behave
    Scenario: Blend apple
      Given I put "apples" in a blender
      When I switch the blender on
      Then it should transform into "apple juice"

    Scenario: Blend orange
      Given I put "oranges" in a blender
      When I switch the blender on
      Then it should transform into "orange juice"