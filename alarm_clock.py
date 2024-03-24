class AlarmClock:


    def __init__(self):
        self.current_time = ('3:30pm')
        self.alarm_on = True
        self.time_alarm_set = ('4:00am')

    def change_current_time(self, set_current_time):
        self.current_time = set_current_time

    def turn_alarm_on(self):
        self.alarm_on = True

    def turn_alarm_off(self):
        self.alarm_on = False

    def change_alarm_time(self, set_alarm_time):
        self.time_alarm_set = set_alarm_time

