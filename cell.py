from enum import Enum


class State(Enum):
    Used = 0
    Unused = 1
    Expire = 2


class Cell:
    def __init__(self, prev: "Cell" = None):
        self.candidates = {i: State.Unused for i in range(9)}
        self.prev = prev

    @property
    def current(self):
        for candidate, state in self.candidates.items():
            if state == State.Used:
                return candidate
        return None

    def expire(self, candidate):
        self.candidates[candidate] = State.expire

    def delete(self, candidate):
        self.candidates.pop(candidate)

    def delete_list(self, candidates_list: set):
        for candidate in candidates_list:
            self.delete(candidate)

    def refresh(self, candidates):
        for candidate, state in self.candidates.items():
            if state in (State.Expire, State.Used):
                candidates[candidate] = State.Unused
