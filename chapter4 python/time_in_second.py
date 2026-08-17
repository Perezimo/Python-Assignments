
def seconds_since_midnight(hour, minute, second):

    hour_in_seconds = 3600 * hour

    minute_in_seconds = 60 * minute

    time_in_second = hour_in_seconds + minute_in_seconds + second
   
    return time_in_second
print(seconds_since_midnight(13, 30, 45))
