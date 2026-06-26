from fastapi import APIRouter
from pydantic import BaseModel

from models.cube import Cube
from services.solver import Solver

router = APIRouter()


class SolveRequest(BaseModel):
    state: str


class SolveResponse(BaseModel):
    solution: str


@router.post("/solve", response_model=SolveResponse)
def solve_cube(request: SolveRequest):
    cube = Cube(request.state)
    solution = Solver.solve(cube)
    return SolveResponse(solution=solution)