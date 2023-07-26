from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class InputDoubler(BaseModel):
    to_double: int

class SalaryInput(BaseModel):
    salary: int
    bonus: int
    taxes: int

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}

# http://127.0.0.1:8000/double/
@app.post("/double/")
def doubler(data: InputDoubler):
    result = data.to_double * 2
    return {"result": result}
    
# http://127.0.0.1:8000/salary_calculator/
# http://127.0.0.1:8000/docs/salary_calculator/
@app.post("/salary_calculator/")
def salary_calculator(data: SalaryInput):
    try: 
        result = data.salary + data.bonus - data.taxes
        return {"result": result}
    except TypeError:
        return {"error": "expected numbers, got strings."}
    except KeyError as e:
        return {"error": f"3 fields expected (salary, bonus, taxes). You forgot: {e}."}