class TuringMachine:
    def __init__(self, lenth: int) -> None:
        self.state_dict: dict = {}
        self.current_state: str | None = None
        self.index: int = 0
        self.lenth: int = lenth - 1

    def add_state(self, name: str, rules: list):
        self.state_dict[name] = rules

    def run(self, input: str):
        state = self.state_dict.get(self.current_state)
        if state is None:
            return
        write, offset, next_state = state[int(input)]
        self.current_state = next_state
        self.index += offset
        if self.index > self.lenth:
            self.index -= self.lenth + 1
        elif self.index < 0:
            self.index += self.lenth + 1
        return write, offset
