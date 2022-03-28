def is_leap(year):
    """
    This function return True if it's leap year .
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    This function will return the days for the year .
    """
    if 0 < month < 12:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year) and month == 2:
            return 29
        return month_days[month - 1]
    return "Invalid input"


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


