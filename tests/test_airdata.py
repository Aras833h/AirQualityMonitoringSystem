from src.models.air_data import AirData

def test_create_airdata():
    data = AirData(45, 80, 2.5, 30)
    assert data.pm25 == 45

def test_calculate_aqi():
    data = AirData(45, 80, 2.5, 30)
    assert data.calculate_aqi() == 80

def test_aqi_positive():
    data = AirData(30, 40, 1.5, 20)
    assert data.calculate_aqi() >= 0