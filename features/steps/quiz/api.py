import requests

from datamodel import Question, Answer


class BaseAPI:
    def get_questions(self) -> list[Question]:
        raise NotImplementedError

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError


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


