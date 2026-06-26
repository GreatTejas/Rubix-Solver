import kociemba
from models.cube import Cube

class Solver:
    @staticmethod
    def solve(cube: Cube):
        if cube.is_solved():
            return ""

        return kociemba.solve(cube.state)