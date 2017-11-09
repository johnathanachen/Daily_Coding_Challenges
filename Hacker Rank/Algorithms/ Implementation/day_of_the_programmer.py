def find_calender_system(year):
    """ Given calendar year,finds the calendar system to the year """
    if year in range(1700, 1918):
        calendar_system = {"Gregorian": year}
    elif year in range(1918, 2701):
        calendar_system = {"Julian": year}
    return calendar_system

def check_leap_year(calendar_system):
    """ Given the year of the calendar_system, check if the year is a leap year """
    calendar_name = ''.join(calendar_system.keys())
    if calendar_name == "Gregorian":
        calender_year = calendar_system["Gregorian"]
        if calender_year % 400 == 0:
            if calender_year % 4 == 0 and calender_year % 100 != 0:
                print(calendar_name, "is a leap year")
    elif calendar_name == "Julian":
        calender_year = calendar_system["Julian"]
        if calender_year % 4 == 0:
            print(calendar_name, "is a leap year")

def main():
    calendar_system = find_calender_system(2000)
    check_leap_year(calendar_system)

start = main()
