"""module to test all functions in stats.py"""
import time
import random
import bikeshare.stats as st

def test():
    while True:
            # choose a random city
            city = random.choice(list(st.CITY_DATA.keys()))
            start_time=time.time()
            # load city into DataFrame
            df_orig = st.load_city(city)
            print(city,"\nData loaded in %s seconds." % (time.time() - start_time))

            # choose random month and day
            month = random.choice([st.conv.int_to_month(random.randint(1,6)),'all'])
            day = random.choice([st.conv.int_to_day(random.randint(0,6)),'all'])
            start_time=time.time()
            #subset DataFrame based on filters
            df, month_filter_set, day_filter_set = st.adjust_timeframe(df_orig,month,day)
            print()
            print(month,day,"\nData reloaded in %s seconds." % (time.time() - start_time))

            print('\nCalculating The Most Frequent Times of Travel...\n')
            start_time = time.time()
            print(st.time_stats(df,month_filter_set, day_filter_set))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            print('\nCalculating The Most Popular Stations and Trip...\n')
            start_time = time.time()
            print(st.station_stats(df))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            print('\nCalculating Trip Duration Statistics...\n')
            start_time = time.time()
            print(st.trip_duration_stats(df))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            print('\nCalculating User Statistics...\n')
            start_time = time.time()
            print(st.user_stats(df))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            restart = input('\nWould you like to try another test?(y or n).\n')
            if restart.lower() != 'y':
                break

if __name__ == '__main__':
    test()
