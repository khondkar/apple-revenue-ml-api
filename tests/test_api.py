from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


VALID_REQUEST = {
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
    "total_apple_proxy_imports_usd_yoy_lag1": 7.3,
}


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict_valid_request():
    response = client.post("/predict", json=VALID_REQUEST)

    assert response.status_code == 200

    response_data = response.json()

    assert "predicted_aapl_revenue_yoy" in response_data
    assert "model_status" in response_data
    assert isinstance(
        response_data["predicted_aapl_revenue_yoy"],
        float,
    )


def test_predict_missing_field():
    invalid_request = VALID_REQUEST.copy()
    invalid_request.pop("aapl_revenue_lag1")

    response = client.post("/predict", json=invalid_request)

    assert response.status_code == 422


def test_predict_invalid_data_type():
    invalid_request = VALID_REQUEST.copy()
    invalid_request["aapl_revenue_lag1"] = "not-a-number"

    response = client.post("/predict", json=invalid_request)

    assert response.status_code == 422