from datetime import datetime

# # x = datetime.datetime.now()


def r(b):
    today = date.today()
    years = abs(today.year-b.year)
    if today.month < b.month:
        years = years-1
    else:
        years = years
    days = abs(today.day-b.day)
    months = abs(today.month-b.month)
    print(f"{years}years,{days}days,{months}months")
#     # print(days)
#     # print(months)
#     # print(f"{today.year - b.year}")
# # print(today)


date_entry = input('Enter a date (i.e. year,month,date): ')
year, month, day = map(int, date_entry.split('-'))
date = datetime(year, month, day)
# print(date)

print(r(date))
# year = int(input('Enter a year'))
# month = int(input('Enter a month'))
# day = int(input('Enter a day'))
# date1 = datetime.date(year, month, day)

# from datetime import datetime
