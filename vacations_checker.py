
from datetime import datetime
from vacations_calendar import CALENDAR

def check(date_str):
    try:
        vacation_date = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError as error:
        print(f"Incorrect data format {date_str}, should be DD/MM/YYYY")
        return 'NoneType'

    search_date = vacation_date.strftime("%d.%m")
    if search_date not in CALENDAR.keys():
        return None
    else:
        return CALENDAR[search_date]
 



# print(check('01/05/2023'))
