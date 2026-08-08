def is_leap_year(year):
    """This functions takes the year as input and provides an output if its Leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
output = is_leap_year(int(input()))
print(output)