from behave import *
from quiz_game import QuizGame, ConsolePlayer, QuizAPI, QUIZ_URL

@given(u'A quiz program')
def step_impl(context):
    quiz_player = ConsolePlayer()
    quiz_api = QuizAPI(QUIZ_URL)
    quiz_game = QuizGame(quiz_api, quiz_player)


@given(u'There is one question')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given There is one question')


@given(u'Answer 1 is correct')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Answer 1 is correct')


@when(u'The user answers 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user answers 1')


@when(u'The program is run')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The program is run')


@then(u'The result should be 1 of 1 questions correct')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The result should be 1 of 1 questions correct')
