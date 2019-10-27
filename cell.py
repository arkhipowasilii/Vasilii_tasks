from enum import Enum


class State(Enum):
    Used = 0
    Unused = 1
    Expire = 2
    Excluded = 3


class Cell:
    def __init__(self, prev: "Cell" = None):
        self.candidates = {i: State.Unused for i in range(1, 10)}
        self.prev = prev

    @property
    def current(self) -> int or None:
        for candidate, state in self.candidates.items():
            if state == State.Used:
                return candidate
        return None

    def expire(self, candidate):
        if candidate in self.candidates:
            self.candidates[candidate] = State.Expire

    def exclude(self, candidate: int):
        if candidate in self.candidates:
            self.candidates[candidate] = State.Excluded

    def use(self, candidate: int):
        if candidate in self.candidates:
            self.candidates[candidate] = State.Used

    def delete(self, candidate):
        self.candidates.pop(candidate)

    def delete_list(self, candidates_list: set):
        for candidate in candidates_list:
            self.delete(candidate)

    def change_used(self, candidate: int) -> int:
        for old_candidate, state in self.candidates.items():
            if state == State.Used:
                self.expire(old_candidate)
                self.use(candidate)
                return old_candidate

    def refresh_one(self, candidate):
        if candidate in self.candidates.keys():
            if self.candidates[candidate] == State.Excluded:
                self.candidates[candidate] = State.Unused

    def refresh_all(self, states: list):
        for candidate, state in self.candidates.items():
            if state in states:
                self.candidates[candidate] = State.Unused

    def get_unused(self):
        unused_candidates = []
        for candidate, state in self.candidates.items():
            if state == State.Unused:
                unused_candidates.append(candidate)
        return unused_candidates
