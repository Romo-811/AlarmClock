from alarm_clock import AlarmClock

alarm_clock_one = AlarmClock()

print("Current time is " + alarm_clock_one.current_time)

alarm_clock_one.change_current_time(input())

print("New time is " + alarm_clock_one.current_time)

alarm_clock_one.change_alarm_time(input())

print("Alarm is now set for " + alarm_clock_one.time_alarm_set)

print(alarm_clock_one.alarm_on)

alarm_clock_one.turn_alarm_off()

print(alarm_clock_one.alarm_on)

alarm_clock_one.turn_alarm_on()

print(alarm_clock_one.alarm_on)
