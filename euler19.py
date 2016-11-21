import datetime


def sundays_on_1st_of_month(start_date, end_date):
    current_date = start_date
    count = 0
    while current_date <= end_date:
        if current_date.day == 1 and current_date.weekday() == 6:
            count += 1
        current_date += datetime.timedelta(days=1)
    return count


def euler19():
    return sundays_on_1st_of_month(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31))
