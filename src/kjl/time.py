import datetime

def get_time_from_timestamp(timestamp: int, timedelta: int = 9):
    dt = datetime.datetime.fromtimestamp(
        timestamp, 
        datetime.timezone(datetime.timedelta(hours=timedelta))
    )
    return dt

