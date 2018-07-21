def retdf(df, city, start):
    """ function to return html of 5 rows of dataFrame

    	Parameters:
			df  	(pandas DataFrame)			:DataFrame to be sliced
			city 	(str)						:city that df corresponds to
			start 	(int)						:starting row index from where to slice		

		Returns:
			html of table corresponding to 5 rows of df	
    """
    if city == 'washington':
        end = 7
    else:
        end = 9
    df =  df.iloc[start:start+5,1:end]
    # convert df to html table
    return df.to_html(classes="table table-striped")
