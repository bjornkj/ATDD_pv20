from api import QuizAPI, BaseAPI
from random import randint


QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Player:
    def ask_num(self, n):
        raise NotImplementedError


class ConsolePlayer(Player):
    def ask_num(self, n):
        while True:
            try:
                res = int(input(">"))
                if 1 <= res <= n:
                    return res
            except ValueError:
                pass


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
            print(question.prompt)
            print(f"{question.percent_correct()} användare svarade rätt på frågan")
            for i, answer in enumerate(question.answers, start=1):
                print(f"[{i}] {answer}")
            self.questions_asked += 1
            user_answer = self.player.ask_num(question.num_answers)
            if question.answers[user_answer - 1].correct:
                print("Correct!")
                self.questions_correct += 1
            print("-" * 80)
        print(f"You answered {self.questions_correct} of {self.questions_asked} correct!")


if __name__ == '__main__':
    q_api = QuizAPI(QUIZ_URL)
    p = ConsolePlayer()
    quiz = QuizGame(q_api, p)
    quiz.run()
