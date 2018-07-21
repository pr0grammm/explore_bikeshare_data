#import Flask instance i.e app
from bikeshare import app
from bikeshare import stats as st
from bikeshare import rawdata as rd
from flask import render_template, request, url_for
from bikeshare.icons import icond

df_orig = None
df = None
current_city = None #city currently loaded in df

#home page
@app.route('/')
def index():
        return render_template('home.html')

# route to handle form submit
@app.route('/postdata', methods = ['post'])
def postdata():
    global current_city, df_orig, df
    data = request.form

    #get parameters
    city=data['city']
    month = data['month']
    day = data['day']

    #get DataFrame
    if city != current_city:
        df_orig = st.load_city(city)
        current_city=city

    # get modified DataFrame
    df, month_filter_set, day_filter_set = st.adjust_timeframe(df_orig, month, day)

    if data['submit'] == 'Get Statistics':
        #calculate statistics
        time_stats = st.time_stats(df, month_filter_set, day_filter_set)
        station_stats = st.station_stats(df)
        trip_duration_stats = st.trip_duration_stats(df)
        user_stats = st.user_stats(df)

        #return page
        page ='stats.html'
        return render_template(page, Time_stats=time_stats,\
        Station_stats=station_stats, Trip_duration_stats=trip_duration_stats,\
        User_stats=user_stats, Icond=icond, trim_blocks =True)

    elif data['submit'] == 'View Raw Data':
        #get first 5 rows of DataFrame
        table= rd.retdf(df,current_city,0)
        page = 'viewraw.html'
        return render_template(page,City=city, \
        Table = table, trim_blocks=True)


@app.route('/gimmeHTML/<int:start>')
def gimmeHTML(start):
    """get HTML corresponding to 5 rows of DataFrame"""
    dfhtml= rd.retdf(df, current_city, start)
    return dfhtml
