from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from brake_model import brake_analysis

from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BrakeInputs(BaseModel):
    pedal_force: float
    pedal_ratio: float

    front_mc_diameter: float
    rear_mc_diameter: float

    front_piston_count: int
    rear_piston_count: int

    front_caliper_diameter: float
    rear_caliper_diameter: float

    front_rotor_radius: float
    rear_rotor_radius: float

    front_balance_percent: float

    vehicle_mass: float

    front_tire_radius: float
    rear_tire_radius: float

    front_pad_mu: float
    rear_pad_mu: float

    wheelbase: float
    cg_height: float

    tire_mu: float

    front_static_weight_percent: float
    
@app.get("/")
def home():
    return {"message": "Brake Analysis API Running"}

@app.post("/calculate")
def calculate(data: BrakeInputs):

    results = brake_analysis(data.model_dump())

    return results