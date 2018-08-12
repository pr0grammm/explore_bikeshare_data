#import Flask instance i.e app
from bikeshare import app
from bikeshare import stats as st
from bikeshare import rawdata as rd
from flask import render_template, request, url_for, session
from bikeshare.icons import icond

#home page
@app.route('/')
def index():
        return render_template('home.html')

# route to handle form submit
@app.route('/postdata', methods = ['post'])
def postdata(start =0):

	if request.method == 'POST':
		data = request.form
		#get parameters
		city=data['city']
		month = data['month']
		day = data['day']
		session['city'] = city
		session['month'] = month
		session['day'] = day;
		#get DataFrame
		df_orig = st.load_city(city)
		current_city=city
		# get modified DataFrame
		df, month_filter_set, day_filter_set = st.adjust_timeframe(df_orig, month, day)

		if data['submit'] == 'Get Statistics':
			time_stats = st.time_stats(df, month_filter_set, day_filter_set)
			station_stats = st.station_stats(df)
			trip_duration_stats = st.trip_duration_stats(df)
			user_stats = st.user_stats(df)

			page ='stats.html'
			return render_template(page, Time_stats=time_stats,\
			Station_stats=station_stats, Trip_duration_stats=trip_duration_stats,\
			User_stats=user_stats, Icond=icond, trim_blocks =True)

		elif data['submit'] == 'View Raw Data':
			table= rd.retdf(df,current_city,0)
			page = 'viewraw.html'
			return render_template(page,City=city, \
			Table = table, trim_blocks=True)

		

@app.route('/gimmeHTML/<int:start>')
def gimmeHTML(start):
	city=session.get('city',None)
	month = session.get('month',None)
	day = session.get('day',None)
	df_orig = st.load_city(city)
	current_city=city
	# get modified DataFrame
	df, month_filter_set, day_filter_set = st.adjust_timeframe(df_orig, month, day)
	table= rd.retdf(df,city,start)
	return table