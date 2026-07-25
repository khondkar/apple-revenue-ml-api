from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from app.logger import logger

from app.model_service import generate_prediction


app = FastAPI(
    title="Apple Revenue Forecast API",
    version="1.0.0",
    description="A production-style API for serving Apple revenue forecasts.",
)


class PredictionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    aapl_revenue_lag1: float
    aapl_revenue_qoq_lag1: float
    aapl_revenue_yoy_lag1: float
    audio_hs8518_usd_lag1: float
    audio_hs8518_usd_yoy_lag1: float
    iphone_hs8517_usd_lag1: float
    iphone_hs8517_usd_yoy_lag1: float
    mac_ipad_hs8471_usd_lag1: float
    mac_ipad_hs8471_usd_yoy_lag1: float
    total_apple_proxy_imports_usd_lag1: float
    total_apple_proxy_imports_usd_yoy_lag1: float


class PredictionResponse(BaseModel):
    predicted_aapl_revenue_yoy: float
    model_status: str


@app.get("/")
def home():
    return {
        "message": "Apple Revenue Forecast API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "apple-revenue-ml-api",
        "version": "1.0.0",
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    try:
        prediction = generate_prediction(request.model_dump())

        logger.info(
            f"Request: {request.model_dump()} | Prediction: {prediction}"
        )

        return PredictionResponse(
            predicted_aapl_revenue_yoy=prediction,
            model_status="production_model"
        )

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please check the server logs."
        )