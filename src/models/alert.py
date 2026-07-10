class Alert:
    def __init__(self):
        pass

    def check_alert(self, aqi):
        if aqi > 100:
            return "هشدار: کیفیت هوا ناسالم است!"
        return "وضعیت هوا عادی است."