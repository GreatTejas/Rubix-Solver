class Cube:
    SOLVED_STATE = (
        "UUUUUUUUU"
        "RRRRRRRRR"
        "FFFFFFFFF"
        "DDDDDDDDD"
        "LLLLLLLLL"
        "BBBBBBBBB"
    )

    def __init__(self, state: str):
        self.state = state

    def is_solved(self):
        return self.state == self.SOLVED_STATE