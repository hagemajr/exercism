from datetime import datetime, timedelta

def add_gigasecond(dt):
    dt1 = dt + timedelta(seconds=1000000000)
    return dt1

add_gigasecond(datetime(2002,1,1))
