Feature: showing off behave
  Scenario: search google for kyh
    Given webbrowser open on google
    When we search for the term kyh
    Then kyh.se is in the search result