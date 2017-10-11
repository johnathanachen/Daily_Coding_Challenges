def time_conversion():
    s = "12:00:01AM" 
    time_zone = list(s)
    if time_zone[1] == "0":
        if "P" in time_zone:
            time_zone.remove('P')
        elif "A" in time_zone:
             time_zone.remove('A')
        time_zone.remove('M')
        str_time_zone = ''.join(time_zone)
        print(time_zone)
    elif "P" in time_zone:
        if time_zone[0] == "1" and time_zone[1] == "2":
            time_zone.remove('P')
            time_zone.remove('M')
            str_time_zone = ''.join(time_zone)
            print(str_time_zone)
        else:
            add_time = ''.join(time_zone[0] + time_zone[1])
            new_time = int(add_time) + 12
            del time_zone[0]
            del time_zone[0]
            time_zone.insert(0,str(new_time))
            time_zone.remove('P')
            time_zone.remove('M')
            str_time_zone = ''.join(time_zone)
            print(str_time_zone)
    elif "A" in time_zone:
        if time_zone[0] == "1" and time_zone[1] == "2":
            time_zone.remove('A')
            time_zone.remove('M')
            time_zone.remove("1")
            time_zone.remove("2")
            time_zone.insert(0, "0")
            time_zone.insert(0, "0")
            str_time_zone = ''.join(time_zone)
            print(str_time_zone)
        else:
            time_zone.remove('A')
            time_zone.remove('M')
            str_time_zone = ''.join(time_zone)
            print(str_time_zone)

time_conversion()