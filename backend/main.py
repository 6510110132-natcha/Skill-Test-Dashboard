from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_daily_reports, parse_new_employees, merge_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/employees")
def get_employees():
    interview_data = parse_daily_reports("./data")
    new_employees = parse_new_employees("./data/New Employee_202502.xlsx")
    merged = merge_data(new_employees, interview_data)
    return merged
