class AirData:
    def __init__(self, pm25, pm10, co, no2):
        self.pm25 = pm25
        self.pm10 = pm10
        self.co = co
        self.no2 = no2

    def calculate_aqi(self):
        return max(self.pm25, self.pm10)