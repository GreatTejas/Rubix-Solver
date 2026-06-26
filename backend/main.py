from fastapi import FastAPI
from api.solve import router as solve_router

app = FastAPI(
    title="Rubik's Cube Solver",
    version="1.0.0"
)

app.include_router(solve_router)


@app.get("/")
def root():
    return {"message": "Rubik's Cube Solver API"}