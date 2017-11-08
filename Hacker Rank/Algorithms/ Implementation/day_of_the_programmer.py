def find_year(year):
    if year in range(1700, 1918):
        calendar_system = {"Gregorian": year}
    elif year in range(1918, 2701):
        calendar_system = {"Julian": year}
    return calendar_system

def check_leap_year(calendar_system):
    calendar_name = ''.join(calendar_system.keys())
    if calendar_name == "Gregorian":
        print("yes")



def main():
    calendar_system = find_year(1704)
    check_leap_year(calendar_system)

start = main()
