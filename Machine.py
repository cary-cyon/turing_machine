"""

{"A1":(B,1,R),
"A0":(B,1,L),
"B1":(A,1,S),
}

"""
from functools import reduce


class TuringMachine:
    """ правило машины rule это словарь """

    def __init__(self, rule, start_state="A", start_position=0):
        self.word_in_processing = ""
        self.rule = rule
        self.state = start_state
        self.work_position = start_position
        self.transitions = {"R": self._move_right,
                            "L": self._move_left,
                            "S": self._stay}

    def do_calculation(self, word, start_position=0):
        self.word_in_processing = word
        self.work_position = start_position
        while True:
            print(self)
            instruction = self.rule.get(self.state + str(self.word_in_processing[self.work_position]))
            if (instruction is None) or len(self.word_in_processing)>30:
                break
            self.state = instruction[0]
            self.word_in_processing[self.work_position] = instruction[1]
            self.transitions.get(instruction[2])()

    def _move_right(self):
        self.work_position += 1
        if self.work_position == len(self.word_in_processing):
            self.word_in_processing += [0]

    def _move_left(self):
        self.work_position -= 1
        if self.work_position == -1:
            self.word_in_processing = [0] + self.word_in_processing
            self.work_position = 0

    def _stay(self):
        pass

    def _print_self(self):
        pass

    def __str__(self):
        res = reduce(lambda x, y: str(x) + str(y), self.word_in_processing)
        res += "\n"
        for index in range(len(self.word_in_processing)):
            res += '.' if index != self.work_position else self.state
        return res
