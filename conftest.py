import pytest

from api.weather_api import WeatherApi


@pytest.fixture
def weather_api():
    """测试用例里只要写 weather_api，就能拿到这个对象。"""
    return WeatherApi()