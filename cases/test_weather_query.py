import os
import pytest
from utils.data_loader import load_yaml_data

current_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(current_dir, "..", "data", "Weather_case.yaml")
DATA = load_yaml_data(yaml_path)


@pytest.mark.parametrize("case", DATA["positive"], ids=lambda c: c["case_id"])
def test_weather_positive(weather_api, case):
    resp = weather_api.query(case["city"], case["future_num"])

    assert resp["reason"] == case["expect"]["reason"]
    assert resp["result"]["city"] == case["expect"]["city"]
    assert len(resp["result"]["future"]) == case["expect"]["future_num"]


@pytest.mark.parametrize("case", DATA.get("negative", []), ids=lambda c: c["case_id"])
def test_weather_negative(weather_api, case):
    resp = weather_api.query(case["city"], case["future_num"])

    assert resp["reason"] == case["expect"]["reason"]