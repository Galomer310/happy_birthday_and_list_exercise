from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age():
    birthdate_input = input("Enter your birthdate (DD/MM/YYYY): ")
    birthdate = datetime.strptime(birthdate_input, "%d/%m/%Y")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age, birthdate

def display_cake(candles):
    print("       " + "i" * candles)
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

age, birthdate = calculate_age()

candles = age % 10
display_cake(candles)

if is_leap_year(birthdate.year):
    print("\nSince you were born in a leap year, here's an extra cake!\n")
    display_cake(candles)
