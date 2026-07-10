from src.models.station import Station
from src.models.air_data import AirData

def test_collect_data_returns_airdata():
    station = Station()
    data = station.collect_data()
    assert isinstance(data, AirData)

def test_collect_data_pm25():
    station = Station()
    data = station.collect_data()
    assert data.pm25 == 85