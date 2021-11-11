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
    ans: list[int]
    last_message: str

    def __init__(self):
        self.ans = []

    def ask_num(self, n) -> int:
        return self.ans.pop(0)

    def send_message(self, message: str):
        self.last_message = message
        print(message)


@given('A quiz program')
def step_impl(context):
    quiz_player = TestPlayer()
    quiz_api = TestAPI()
    quiz_game = QuizGame(quiz_api, quiz_player)
    context.quiz_api = quiz_api
    context.quiz_player = quiz_player
    context.quiz_game = quiz_game


@given('There is one question')
def step_impl(context):
    context.question = Question(1, "", 0, 0, [])
    context.quiz_api.questions.append(context.question)


@given('Answer 1 is correct')
def step_impl(context):
    context.answer = Answer("", True)
    context.question.answers.append(context.answer)


# When The user answers 1 -> step_impl(context, "1")
# When The user answers 2 -> step_impl(context, "2")
# When The user answers Hej -> step_impl(context, "Hej")
# When The user answers 2,1 -> step_impl(context, "2,1")

@when('The user answers {ans}')
def step_impl(context, ans):
    context.quiz_player.ans = list(map(int, ans.split(',')))


@when('The program is run')
def step_impl(context):
    context.quiz_game.run()


@then('The result should be {result}')
def step_impl(context, result):
    last_row = context.quiz_player.last_message
    assert last_row == result, f"'{result}' got '{last_row}'"


@given('a question "{prompt}"')
def step_impl(context, prompt):
    res = []
    for row in context.table:
        res.append(Answer(row['answer'], bool(row['correct'])))
    context.quiz_api.questions.append(Question(1, prompt, 10, 5, res))


@given('question with')
def step_impl(context):
    q_id = len(context.quiz_api.questions) + 1
    q_row = context.table[0]
    q = Question(q_id, q_row['prompt'], int(q_row['times_asked']), int(q_row['times_correct']), [])
    for a in context.table[1:]:
        q.answers.append(Answer(a['answer'], a['correct'] == "True"))

    context.quiz_api.questions.append(q)


@then(u'Fail the test')
def step_impl(context):
    assert False
