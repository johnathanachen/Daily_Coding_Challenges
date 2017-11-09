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
                return True
            else:
                return False
    elif calendar_name == "Julian":
        calender_year = calendar_system["Julian"]
        if calender_year % 4 == 0:
            return True
        else:
            return False

def print_256th_day(is_leap_year):
    # normal_years = [31,28,31,30,31,30,31,31]
    # leap_year = [31,29,31,30,31,30,31,31]
    if is_leap_year:
        print("12.09."+str(year))
    else:
        print("13.09."+str(year))

year = 2017
def main():
    """ Start Program """
    calendar_system = find_calender_system(year)
    is_leap_year = check_leap_year(calendar_system)
    print_256th_day(is_leap_year)


start = main()
