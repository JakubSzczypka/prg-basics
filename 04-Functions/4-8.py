def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    elif time_format == '12':
        period = 'am'
        display_hour = hours
        if hours == 0:
            display_hour = 12
        elif hours == 12:
            period = 'pm'
        elif hours > 12:
            display_hour = hours - 12
            period = 'pm'
        return f"{display_hour}:{minutes:02d}{period}"

if __name__ == "__main__":
    print(time_string(15, 38, '24'))
    print(time_string(8, 3, '24'))
    print(time_string(0, 5, '24'))
    print(time_string(11, 15, '12'))
    print(time_string(0, 7, '12'))
    print(time_string(7, 30, '12'))
    print(time_string(12, 46, '12'))
    print(time_string(13, 10, '12'))
    print(time_string(19, 2, '12'))