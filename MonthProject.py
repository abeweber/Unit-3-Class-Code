'''
Name: Abe Weber
Date: 10/22/24
Assignment: Unit 2 and 3 Project
'''
user_month = input("Enter the name of the month:")
month = user_month.title()
day = int(input("Enter the day (1-31):"))

if month == "January" or month == "February":
    print(f"{month} {day} is in Winter")
elif month == "March" and 0 < day < 20:
    print(f"{month} {day} is in Winter")
elif month == "March" and 32 > day >= 20:
    print(f"{month} {day} is in Spring")
elif month == "April" or month == "May":
    print(f"{month} {day} is in Spring")
elif month == "June" and 0 < day < 21:
    print(f"{month} {day} is in Spring")
elif month == "June" and 32 > day > 21:
    print(f"{month} {day} is in Summer")
elif month == "July" or month == "August":
     print(f"{month} {day} is in Summer")
elif month == "September" and 0 < day < 22:
     print(f"{month} {day} is in Summer")
elif month == "September" and 32 > day > 22:
     print(f"{month} {day} is in Fall")
elif month == "October" or month == "November":
    print(f"{month} {day} is in Fall")
elif month == "December" and 0 < day < 21:
     print(f"{month} {day} is in Fall")
elif month == "December" and 32 > day > 21:
     print(f"{month} {day} is in Winter")
else:
    print("Invalid date. Please try again")