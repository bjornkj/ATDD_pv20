from typing import Union


class Blender:
    thing: str
    result: str

    def __init__(self):
        self.thing = ""
        self.result = ""

    def add(self, thing):
        self.thing = thing

    def switch_on(self):
        if self.thing == "apples":
            self.result = "apple juice"
        elif self.thing == "oranges":
            self.result = "orange juice"
