# Apple Revenue Forecast API

## Overview

A production-style Machine Learning API that predicts Apple's quarterly year-over-year revenue growth using U.S. import proxy data and historical financial features.

The project demonstrates an end-to-end ML deployment workflow, including model training, REST API development, automated testing, containerization, and continuous integration.

---

## Features

- LightGBM regression model
- FastAPI REST API
- Pydantic request validation
- Model serialization with Joblib
- Structured logging
- Exception handling
- Automated API testing with Pytest
- Docker containerization
- GitHub Actions CI/CD pipeline
- Interactive Swagger documentation

---

## Project Architecture

```
                Historical Data
                       │
                       ▼
            Feature Engineering
                       │
                       ▼
            LightGBM Model Training
                       │
                       ▼
            Saved Joblib Model
                       │
                       ▼
                 FastAPI Server
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
      Swagger UI            REST Clients
                       │
                       ▼
                 JSON Prediction
```

---

## Technology Stack

- Python
- FastAPI
- LightGBM
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Pytest
- Docker
- GitHub Actions

---

## API Endpoints

### Home

```
GET /
```

Returns API information.

---

### Health Check

```
GET /health
```

Returns API health status.

---

### Prediction

```
POST /predict
```

Example Request

```json
{
  "aapl_revenue_lag1": 124300000000,
  "aapl_revenue_qoq_lag1": 15.2,
  "aapl_revenue_yoy_lag1": 4.0,
  "audio_hs8518_usd_lag1": 1200000000,
  "audio_hs8518_usd_yoy_lag1": 6.5,
  "iphone_hs8517_usd_lag1": 45000000000,
  "iphone_hs8517_usd_yoy_lag1": 8.0,
  "mac_ipad_hs8471_usd_lag1": 7200000000,
  "mac_ipad_hs8471_usd_yoy_lag1": 5.4,
  "total_apple_proxy_imports_usd_lag1": 53400000000,
  "total_apple_proxy_imports_usd_yoy_lag1": 7.3
}
```

Example Response

```json
{
  "predicted_aapl_revenue_yoy": 0.156,
  "model_status": "production_model"
}
```

---

## Running Locally

Clone the repository

```bash
git clone https://github.com/khondkar/apple-revenue-ml-api.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the API

```bash
uvicorn app.main:app --reload
```

Open Swagger

```
http://localhost:8000/docs
```

---

## Docker

Build

```bash
docker build -t apple-revenue-api .
```

Run

```bash
docker run -p 8000:8000 apple-revenue-api
```

---

## Testing

Run automated tests

```bash
pytest -v
```

---

## Continuous Integration

Every push automatically:

- Installs dependencies
- Runs automated API tests
- Validates the application
- Reports build status through GitHub Actions

---

## Future Improvements

- Cloud deployment
- Batch prediction endpoint
- Model versioning
- Automated retraining pipeline
- Monitoring and alerting
- Authentication and rate limiting

---

## Author

Kamal Khondkar

GitHub

https://github.com/khondkar
