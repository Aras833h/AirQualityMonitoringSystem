from src.models.alert import Alert

def test_alert_created():
    alert = Alert()
    assert alert is not None

def test_high_aqi_alert():
    alert = Alert()
    result = alert.check_alert(150)
    assert "هشدار" in result

def test_normal_aqi():
    alert = Alert()
    result = alert.check_alert(50)
    assert "عادی" in result