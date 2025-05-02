from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import stalls, stations, payments, reports

app = FastAPI(title="Catering Stalls Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stalls.router, prefix="/stalls", tags=["Stalls"])
app.include_router(stations.router, prefix="/stations", tags=["Stations"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Optional: Add a main entry point for running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

   

