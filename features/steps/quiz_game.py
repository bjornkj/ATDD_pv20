import json

import requests

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Answer:
    answer: str
    correct: bool

    def __init__(self, answer, correct):
        self.answer = answer
        self.correct = correct

    def __str__(self):
        return self.answer


class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list[Answer]

    def __init__(self, id_, prompt, times_asked, times_correct, answers: list[Answer]):
        self.id = int(id_)
        self.prompt = prompt
        self.times_asked = int(times_asked)
        self.times_correct = int(times_correct)
        self.answers = answers

    def percent_correct(self) -> str:
        if self.times_asked == 0:
            return "No answers yet"
        else:
            return f"{self.times_correct / self.times_asked:.0%}"

    @property
    def num_answers(self):
        return len(self.answers)


class BaseAPI:
    def get_questions(self) -> list[Question]:
        raise NotImplementedError

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError


class BjornsFakeAPI(BaseAPI):
    def get_questions(self) -> list[Question]:
        return [Question(1, "En enkel fråga", 1, 2, [Answer("Ett rätt svar", True),
                                                     Answer("Också rätt", True)])]


class BjornsFileAPI(BaseAPI):
    def get_questions(self) -> list[Question]:
        with open("questions.json") as f:
            questions = json.load(f)['questions']
            return [self._parse_question(q) for q in questions]

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError

    def _parse_answer(self, a) -> Answer:
        return Answer(a['answer'], a['correct'])

    def _parse_answers(self, answers) -> list[Answer]:
        return [self._parse_answer(a) for a in answers]

    def _parse_question(self, q) -> Question:
        return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], self._parse_answers(q['answers']))


class QuizAPI(BaseAPI):
    url: str

    def __init__(self, url):
        self.url = url

    def get_questions(self) -> list[Question]:
        questions = requests.get(self.url).json()['questions']
        return [self._parse_question(q) for q in questions]

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError

    def _parse_answer(self, a) -> Answer:
        return Answer(a['answer'], a['correct'])

    def _parse_answers(self, answers) -> list[Answer]:
        return [self._parse_answer(a) for a in answers]

    def _parse_question(self, q) -> Question:
        return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], self._parse_answers(q['answers']))


class Player:
    @staticmethod
    def ask_num(n) -> int:
        raise NotImplementedError

    @staticmethod
    def send_message(message: str):
        raise NotImplementedError


class ConsolePlayer(Player):
    @staticmethod
    def ask_num(n) -> int:
        while True:
            try:
                res = int(input(">"))
                if 1 <= res <= n:
                    return res
            except ValueError:
                pass

    @staticmethod
    def send_message(message: str):
        print(message)


class QuizGame:
    quiz_api: BaseAPI
    player: Player
    questions_asked: int
    questions_correct: int

    def __init__(self, quiz_api: BaseAPI, player: Player):
        self.quiz_api = quiz_api
        self.player = player
        self.questions_asked = 0
        self.questions_correct = 0

    def run(self):
        for question in self.quiz_api.get_questions():
            self.player.send_message(question.prompt)
            self.player.send_message(f"{question.percent_correct()} användare svarade rätt på frågan")
            for i, answer in enumerate(question.answers, start=1):
                self.player.send_message(f"[{i}] {answer}")
            self.questions_asked += 1
            user_answer = self.player.ask_num(question.num_answers)
            if question.answers[user_answer - 1].correct:
                self.player.send_message(f"{user_answer} is Correct!")
                self.questions_correct += 1
            else:
                self.player.send_message(f"{user_answer} is Wrong!")
            self.player.send_message("-" * 80)
        self.player.send_message(f"You answered {self.questions_correct} of {self.questions_asked} correct!")




if __name__ == '__main__':
    q_api = QuizAPI(QUIZ_URL)
    # q_api = BjornsFakeAPI()
    # q_api = BjornsFileAPI()
    p = ConsolePlayer()
    quiz = QuizGame(q_api, p)
    quiz.run()
