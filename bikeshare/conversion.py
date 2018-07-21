"""
contains functions for conversion between string and int representations\
of day and month
"""
def day_to_int(day):
    """return int representation of day"""

    d = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, \
    'saturday':5, 'sunday':6}

    return d[day]

def int_to_day(num):
    """return day associated with an int value"""

    d = { 0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', \
    5:'saturday', 6:'sunday'}

    return d[num]

def month_to_int(month):
    """return int representation of month"""

    d = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}

    return d[month]

def int_to_month(num):
    """return month associated with an int value"""

    d = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}

    return d[num]
