from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/calculate")
async def calculate(op1: float, op2: float, operator: str):
    result = None
    if operator == 'add':
        result = op1 + op2
    elif operator == 'subtract':
        result = op1 - op2
    elif operator == 'multiply':
        result = op1 * op2
    elif operator == 'divide':
        if op2 == 0:
            return {"error": "Cannot divide by zero"}
        result = op1 / op2
    else:
        return {"error": "Invalid operator"}
    
    return {"result": result}
