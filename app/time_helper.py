import calendar
from datetime import datetime


now = datetime.now()
year = now.year
month = now.month
month_name = calendar.month_name[month]

days_in_month = calendar.monthrange(year, month)[1]


def now_day() -> int:
    return now.day
