
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import add, divide, multiply, subtract

api = FastAPI(title="Python CI/CD Demo API", version="0.3.0")


class Calculation(BaseModel):
    a: float
    b: float
    operation: str


@api.get("/health")
def health():
    return {"status": "ok"}


@api.post("/calculate")
def calculate(request: Calculation):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if request.operation not in operations:
        raise HTTPException(
            status_code=400,
            detail="Unsupported operation",
        )

    try:
        result = operations[request.operation](request.a, request.b)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {"operation": request.operation, "result": result}
