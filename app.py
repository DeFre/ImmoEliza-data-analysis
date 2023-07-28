import json
import pandas as pd
import xgboost as xg
from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import Union, Any, Dict, Optional, Tuple

# http://127.0.0.1:8000/docs/

class ImmoInput(BaseModel):
    #immo_code: Optional[int] = None         #this value is not used in the model, but is included for easy verification
    #price: Optional[int] = None             #this value is not used in the model, but is included for easy verification
    #property_type: Optional[str] = None     #if this is not filled out the xg_model_full will be used
    #property_subtype: Optional[str] = None  
    primary_energy_consumption: int
    furnished: int
    terrace: int
    terrace_surface: int
    plot_surface: int
    living_room_surface: int
    frontages: int
    construction_year: int
    bedrooms: int
    bathrooms: int
    shower_rooms: int
    office: int
    toilets: int

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'Welcome to the ImmoEliza House Price Predictor',
            'INFO': 'to use this API, please provide the following features as integers',
            "data-format":{     
                "primary_energy_consumption": "integer",
                "furnished": "integer",
                "terrace": "integer",
                "terrace_surface": "integer",
                "plot_surface": "integer",
                "living_room_surface": "integer",
                "frontages": "integer",
                "construction_year": "integer",
                "bedrooms": "integer",
                "bathrooms": "integer",
                "shower_rooms": "integer",
                "office": "integer",
                "toilets": "integer"
                }

            }

@app.post("/price_predictor/")
def price_predictor(data: ImmoInput):
    model = xg.Booster()
    model.load_model("models/xg_model_full.json")
    test_df = pd.DataFrame(data.model_dump(), index=[0])
    xgtest = xg.DMatrix(test_df.values)
    prediction = float(model.predict(xgtest))
    return {f"Based on the input provided, we expect this property to be valued at € {prediction}."}