from src.models.air_data import AirData

class Station:
    def collect_data(self):
        return AirData(
            pm25=85,
            pm10=120,
            co=4.5,
            no2=70
        )