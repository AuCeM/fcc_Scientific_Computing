def add_time(init_time, elapsed_time,initial_day=''):
    week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    
    # obtain hours, minutes and daytime separately
    colon_index = init_time.index(":")
    init_hours = int(init_time[:colon_index])
    init_mins = int(init_time[colon_index + 1:colon_index + 3])
    init_am_pm = init_time[init_time.index(" ")+1:]
        
    # elapsed_time hours and minutes
    elapsed_hours = int(elapsed_time[:elapsed_time.index(":")])
    elapsed_mins = int(elapsed_time[elapsed_time.index(":")+1:])
    
    # obtain total amount of hours and minutes, obtain hours and minutes on a 12 hour basis 
    total_mins = init_mins + elapsed_mins
    hours = init_hours + elapsed_hours
    
    added_hours = 0
    if total_mins >= 60:
        added_hours = total_mins // 60
        remaining_min = total_mins % 60
    else:
        remaining_min = total_mins
    if remaining_min < 10:
        remaining_min = f'0{remaining_min}'
    
    # calculating days that will be added, as well as remaining hours for our calculator...also correcting 00:mm 
    added_days = 0
    half_day = 0
    remaining_hours = 0
    total_hours = hours + added_hours
    if total_hours >= 24:
        added_days = total_hours // 24
        remaining_hours = total_hours % 24
        if remaining_hours > 12:
            half_day = remaining_hours
            remaining_hours = remaining_hours % 12
    elif total_hours >= 12 and total_hours < 24:
        remaining_hours = total_hours % 12
    elif total_hours < 12:
        remaining_hours = total_hours
    if remaining_hours == 0:
        remaining_hours = "12"    
    
    # obtaining new_time while no initial day is provided
    n = total_hours // 12
    am_or_pm = ''
    new_time = ''
    if initial_day == '':
        # first three conditions are while total_hours are less than 24, and the last one with the nested if/elifs is for total_hours >= 24
        if total_hours < 12 and total_mins < 60:
            am_or_pm = init_am_pm
            new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}"
        elif total_hours >= 12 and total_hours < 24 and init_am_pm == 'AM':
            am_or_pm = 'PM'
            new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}"
        elif total_hours >= 12 and total_hours < 24 and init_am_pm == 'PM':
            am_or_pm = 'AM'
            new_time = f"{remaining_hours}:{remaining_min} {am_or_pm} (next day)"
        elif total_hours >= 24:
            if init_am_pm == 'AM':
                if n % 2 != 0:
                    am_or_pm = 'PM'
                else:
                    am_or_pm = 'AM'
            else:
                if n % 2 != 0:
                    am_or_pm = 'AM'
                else:
                    am_or_pm = 'PM'
            
            if added_days == 1 and init_am_pm == 'PM' and n % 2 != 0:
                added_days += 1
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm} ({added_days} days later)"
            elif added_days == 1:
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm} (next day)"
            elif added_days > 1 and half_day < 24 - init_hours:
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm} ({added_days} days later)"
            elif added_days > 1 and half_day >= 24 - init_hours:
                added_days += 1
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm} ({added_days} days later)"
    
    # obtaining new_time while initial_day is provided
    if initial_day != "":
        initial_day = initial_day.lower().capitalize()
        future_day = ''
        for key in week:
            if week[key] == initial_day:
                passing_days = added_days + key
                if passing_days > 7 and half_day >= 24 - init_hours:
                    passing_days = (passing_days + 1) % 7
                elif passing_days > 7:
                    passing_days %= 7
                future_day = week[passing_days]
        # first three conditions are while total_hours are less than 24, and the last one with the nested if/elifs is for total_hours >= 24
        if total_hours < 12 and total_mins < 60:
            am_or_pm = init_am_pm
            new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day}"
        elif total_hours >= 12 and total_hours < 24 and init_am_pm == 'AM':
            am_or_pm = 'PM'
            new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day}"
        elif total_hours >= 12 and total_hours < 24 and init_am_pm == 'PM':
            am_or_pm = 'AM'
            new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day} (next day)"
        elif total_hours >= 24:
            if init_am_pm == 'AM':
                if n % 2 != 0:
                    am_or_pm = 'PM'
                else:
                    am_or_pm = 'AM'
            else:
                if n % 2 != 0:
                    am_or_pm = 'AM'
                else:
                    am_or_pm = 'PM'
            
            if added_days == 1 and init_am_pm == 'PM' and n % 2 != 0:
                added_days += 1
                passing_days += 1
                future_day = week[passing_days]
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day} ({added_days} days later)"
            elif added_days == 1:
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day} (next day)"
            elif added_days > 1 and half_day < 24 - init_hours:
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day} ({added_days} days later)"
            elif added_days > 1 and half_day >= 24 - init_hours:
                added_days += 1
                new_time = f"{remaining_hours}:{remaining_min} {am_or_pm}, {future_day} ({added_days} days later)"
                

    return new_time

add_time('11:50 PM', '60:05','Wednesday')