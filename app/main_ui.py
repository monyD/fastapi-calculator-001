from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI Calculator (with UI)")

# Serve the existing `static/` and `templates/` folders — no changes to your current main.py
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class CalcResult(BaseModel):
    result: float

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    """Render the server-side template located at templates/index.html."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/add", response_model=CalcResult)
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/api/subtract", response_model=CalcResult)
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/api/multiply", response_model=CalcResult)
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/api/divide", response_model=CalcResult)
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}

# Optional consolidated endpoint
@app.get("/api/calculate", response_model=CalcResult)
def calculate(op: str, a: float, b: float):
    op = op.lower()
    if op in ("add", "+"):
        return {"result": a + b}
    if op in ("sub", "-", "subtract"):
        return {"result": a - b}
    if op in ("mul", "*", "multiply"):
        return {"result": a * b}
    if op in ("div", "/", "divide"):
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return {"result": a / b}
    raise HTTPException(status_code=400, detail="Unknown operation")
