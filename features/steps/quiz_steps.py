from behave import *
from quiz_game import QuizGame, ConsolePlayer, QuizAPI, QUIZ_URL, Question, Answer, BaseAPI, Player

# Problem
# 1. Vi får frågor från APIet, hur skall vi mata in våra egna testfrågor
# 2. Programmet väntar sig input från användaren via stdin


class TestAPI(BaseAPI):
    questions: list[Question]

    def __init__(self):
        self.questions = []

    def get_questions(self) -> list[Question]:
        return self.questions


class TestPlayer(Player):
    ans: int
    last_message: str

    def __init__(self):
        self.ans = 1

    def ask_num(self, n) -> int:
        return self.ans

    def send_message(self, message: str):
        self.last_message = message


@given(u'A quiz program')
def step_impl(context):
    quiz_player = TestPlayer()
    quiz_api = TestAPI()
    quiz_game = QuizGame(quiz_api, quiz_player)
    context.quiz_api = quiz_api
    context.quiz_player = quiz_player
    context.quiz_game = quiz_game


@given(u'There is one question')
def step_impl(context):
    context.question = Question(1, "", 0, 0, [])
    context.quiz_api.questions.append(context.question)


@given(u'Answer 1 is correct')
def step_impl(context):
    context.answer = Answer("", True)
    context.question.answers.append(context.answer)


@when(u'The user answers 1')
def step_impl(context):
    context.quiz_player.ans = 1


@when(u'The program is run')
def step_impl(context):
    context.quiz_game.run()


@then(u'The result should be 1 of 1 questions correct')
def step_impl(context):
    expected = "You answered 1 of 1 correct!"
    last_row = context.quiz_player.last_message
    assert last_row == expected, f"'{expected}' got '{last_row}'"
