"""
    module to load csv file into DataFrame
    and compute various statistics
"""
import pandas as pd
import numpy as np
import bikeshare.conversion as conv

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_city(city):
    """
    Load city data into a DataFrame

    Parameters:
        city (str)                  : a key in CITY_DATA dictionary

    Returns:
        df_orig (pandas DataFrame)  : Dataframe loaded with city data
    """

    df_orig = pd.read_csv('./bikeshare/data_files/' + CITY_DATA[city])

    # convert the Start Time column to datetime
    df_orig['Start Time'] = pd.to_datetime(df_orig['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df_orig['month'] = df_orig['Start Time'].dt.month#month b/w  and 6
    df_orig['day_of_week'] = df_orig['Start Time'].dt.dayofweek#day_of_week b/w 0 and 6

    return df_orig


def adjust_timeframe(df_orig, month, day):
    """
    modify dataframe based on time filters

    Parameters:
        df_orig (pandas DataFrame)     : original DataFrame to subset
        month (str)                    : months 'january' through 'june' or 'all'
        day (str)                      : days 'monday' through 'sunday' or 'all'

    Returns:
        df (pandas DataFrame)          : subsetted Dataframe
        month_filter_set (bool)        : True if month != 'all'
        day_filter_set (bool)          : True if day != 'all'
    """
    #initially assume no filters set
    month_filter_set = day_filter_set = False

    #do not modify original dataset
    df = df_orig.copy()

    # filter by month if applicable
    if month != 'all':
        month_number = conv.month_to_int(month)
        df = df[df['month'] == month_number]
        month_filter_set = True

    # filter by day of week if applicable
    if day != 'all':
        day_number = conv.day_to_int(day)
        df = df[df['day_of_week'] == day_number]
        day_filter_set = True

    return df, month_filter_set, day_filter_set


def time_stats(df, month_filter_set, day_filter_set):
    """Displays statistics on the most frequent times of travel."""

    popular_month = popular_day_of_week = popular_start_hour = None

    # find the most common month if applicable
    if(not month_filter_set):
        popular_month = conv.int_to_month(df['month'].mode()[0])
        popular_month = popular_month.title()

    # find the most common day of week if applicable
    if(not day_filter_set):
        popular_day_of_week = conv.int_to_day(df['day_of_week'].mode()[0])
        popular_day_of_week = popular_day_of_week.title()

    # find the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]

    return [('Most common month', popular_month), \
    ('Most common day of week', popular_day_of_week) ,\
    ('Most common hour of day', popular_start_hour)]


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    # find most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # find most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # find most frequent combination of start station and end station trip
    start, end = df.groupby(['Start Station','End Station']).size().idxmax()

    return [('Most common start station', popular_start_station) , \
    ('Most common end station', popular_end_station), \
    ('Most common trip',str(start) + ' -----> ' + str(end))]


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    # find total travel time
    total_travel_time = df['Trip Duration'].sum()

    # find mean travel time
    mean_travel_time = total_travel_time/len(df)

    return [('Total travel time (s)',total_travel_time), \
    ('Average travel time (s)', mean_travel_time)]


def user_stats(df):
    """Displays statistics on bikeshare users."""
    user = gender = age = None

    # find counts of user types
    '''pd.value_counts(df['User Type'])
    Subscriber    238889
    Customer       61110
    Dependent          1
    '''
    user_series = pd.value_counts(df['User Type'])
    user =  list(zip(list(user_series.index), list(user_series)))

    # find counts of gender if applicable
    if 'Gender' in df.columns:
        gender_series = pd.value_counts(df['Gender'])
        gender = list(zip(list(gender_series.index),list(gender_series)))

    # find earliest, most recent, and most common year of birth if applicable
    if 'Birth Year' in df.columns:
        youngest = df['Birth Year'].max().astype(int)
        oldest = df['Birth Year'].min().astype(int)
        common = df['Birth Year'].mode()[0].astype(int)
        age = [('Year of birth of youngest rider',youngest), \
        ('Year of birth of oldest rider', oldest), \
        ('Most common year of birth', common)]

    return [('Counts of each user',user),('Counts of each gender',gender),\
    ('Birth year statistics',age)]
