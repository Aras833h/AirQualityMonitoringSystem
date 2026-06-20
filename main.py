from models.station import Station
from models.alert import Alert
from reports.report import Report

station = Station()
data = station.collect_data()

aqi = data.calculate_aqi()

alert = Alert()
report = Report()

print("----- Air Quality Monitoring System -----")
print(f"PM2.5 : {data.pm25}")
print(f"PM10  : {data.pm10}")
print(f"CO    : {data.co}")
print(f"NO2   : {data.no2}")
print()

print(f"AQI : {aqi}")
print(alert.check_alert(aqi))
print(report.generate(aqi))