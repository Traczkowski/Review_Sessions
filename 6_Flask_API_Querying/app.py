from flask import Flask, jsonify, redirect
import requests
import pandas as pd
import config
import random
import psycopg2 as ps2
import pandas.io.sql as sqlio


"""
An extra note here is that if you don't have a properly confiured config.py 
here, you will have issues with any weather api parts of this flask playground,
if you don't have a database you can connect to that'd prevent the sql portion
from working. Finally, you'll need to add some csv files into the same directory
as this app.py if you want to try to run the pandas portion, so there will be
a little bit of setup and this won't necessarily work right out of the box
until you add those few things. I also got quite a few questions about
ethical scraping at the end of the session. I recommend that you read up from
a large variety of sources about that. Scraping isn't necessarily a part of
every data science workflow, but if you find that you are using it at your
job, you'll want to know a lot about how to do it in a way that is acceptable.
We will be talking about it in class a bit, but as with a lot in this field, 
there is no one correct answer, and it is best to do your due dilligence 
before setting off on a scraping project!

What is robots.txt? https://moz.com/learn/seo/robotstxt

A bit on ethical scraping https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01

The Towards Data Science posts tagged with "Python Flask" https://towardsdatascience.com/tagged/python-flask

To answer Jewell's question that she had regarding the ability to pass 
default function parameters in from app routes I wanted to include this.
Look at the answer with 178 upvotes (it is basically the same as the one with
~330 upvotes but they make it slightly less complex-looking). You'd have to have it
listening on both routes (one with a username being passed, and the other
without the username being passed.) Let me know if you'd want to discuss
that further and we can try to play around with it during office hours or a break.

https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters
"""

app = Flask(__name__)

@app.route('/')
def home_page():
	"""
	Very boring homepage which just shows options.
	"""
	return('<h1>Welcome to the practice Flask playground!</h1><br/>' +\
		'Here are some options that you can pick for now... <br/>' +\
		'1. /weatherV1/ for random weather</br>' +\
		'2. /weatherV2/ larger city list with 2 custom responses</br>' +\
		'3. /weatherV3/ pass in a city name to get the weather!</br>' +\
		'4. /sqlV1/     pass in a number to limit your query on</br>' +\
		'5. /sqlV2/     this has a lot more parameters it can accept</br>' +\
		'6. /pandareaderV1/ allows us to pick which file to get jsons from </br>' +\
		'7. /pandareaderV2/ this would allow file and column </br>' +\
		'8. /NextPageSimulator/ pass in an input to land on a page number and then fly through the pages! </br>')


@app.route('/weatherV1/')
def weather_one():
	"""
	Will get random output from the weather API (passed straight through,
	representing a situation with no internal pipeline, just making the 
	contents of one API pass through another). This can be analagous to a 
	traffic website pinging the google maps api for traffic and then just 
	passing that through their front-end (obviously a much more elegant 
	solution than this)
	"""

	query_url = f'http://api.openweathermap.org/data/2.5/weather?appid={config.api_key}&units=imperial&q='

	cities = ['Atlanta', 'New York', 'Miami', 'Dallas']
	response = requests.get(query_url + cities[random.randint(0,3)]).json()
	return(jsonify(response))



@app.route('/weatherV2/')
def weather_two():
	"""
	This second version of our weather API actually has a slightly larger 
	city list, it will actually add a bit of information to our output, and 
	send information to both the command line as well as the front-end. 
	NOTE: This api will also output two cities and do some simple comparison. 
	The reason I've included a little bit more here is to make it more 
	analagous to a company bringing in outside information, doing something 
	novel with it, and then sending everything through as a json object 
	(either in their own api or to their front-end)
	"""

	query_url = f'http://api.openweathermap.org/data/2.5/weather?appid={config.api_key}&units=imperial&q='

	cities = ['Atlanta', 'Tokyo', 'Miami', 'Dallas', 'London', 'Warsaw', 'New York']
	
	response = requests.get(query_url + cities[random.randint(0,2)]).json()
	response2 = requests.get(query_url + cities[random.randint(3,5)]).json()
	
	response['ExtraParameter'] = 'Always Pass the extra parameter!'
	response2['SecondExtraParam'] = f'This location scores a {random.randint(0,99)}'

	our_response = {'FirstResponse' : response,
					'SecondResponse' : response2}


	if response['main']['feels_like'] > response2['main']['feels_like']:
		print("It feels like " + str(response['main']['feels_like']) + " In the first city" + " and " + str(response2['main']['feels_like']) + " In the second, the first is warmer")
	elif response['main']['feels_like'] < response2['main']['feels_like']:
		print("It feels like " + str(response['main']['feels_like']) + " In the first city" + " and " + str(response2['main']['feels_like']) + " In the second, the second is warmer")
	else:
		print("same temp!")
	return(jsonify(our_response))
	


@app.route('/weatherV3/<city_name>')
def weather_three(city_name):
	"""
	This is a similar setup to the last 2 weather apis, but in this one we 
	were able to make it more consumer-friendly, all you have to do is type
	in a correct city name and it should pull the information right into the 
	front-end for us, this has a little bit of error checking included here 
	(which is a start), but we'd definitely need a lot more before we could 
	consider anything in this activity production ready.
	"""

	query_url = f'http://api.openweathermap.org/data/2.5/weather?appid={config.api_key}&units=imperial&q='

	try:
		response = requests.get(query_url + city_name).json()
		print("Thanks for correctly using the Weather API V3")
		return(jsonify(response))
	except:
		print("You hit an error block! Best of luck picking a new city!")
		return("Please try again with a valid city name!", 404)



@app.route('/sqlV1/<limit_num>/')
def sql_one(limit_num = 50):
	"""
	This version of the sql API allows us to set a number that we want to 
	limit our sample query to, it will also naively set the table result to 
	json (note that you'd want to probably have some more logic in a real 
	sitaution, but turning a pandas table into a json so that it can be used 
	as part of an API can be a powerful tool if you are using it properly. 
	This also demonstrates connection info. I may also show a twist on this 
	where we would also pass in the dbname as well.
	"""

	conn = ps2.connect(
	dbname = config.dbname, \
	host = config.host, \
	port = config.port, \
	user = config.user, \
	password = config.password)

	q1 = f'''SELECT * FROM film ORDER BY film_id DESC LIMIT {limit_num}'''
	data = sqlio.read_sql_query(q1, conn)
	print(data)
	return(data.to_json())
	


@app.route('/sqlV2/<t_name>/<col_name>/<where_adlib>/<limit_num>')
def sql_two(t_name = 'rental', col_name = 'inventory_id', where_adlib = 'first_name', limit_num = 100):
	"""
	This version of the sql API allows several strings to come in that allow 
	you to change table name, column name, a word to drop into your where 
	clause, and then the number by which to limit the number of output rows. 
	The way we'd want to think about this use-case is giving someone that 
	normally wouldn't have access to sql a somewhat more simplified input.
	"""

	conn = ps2.connect(
	dbname = config.dbname, \
	host = config.host, \
	port = config.port, \
	user = config.user, \
	password = config.password)

	"""
	NOTE: There should be a ton of error checking AND sanitization done at 
	this point if you're not in an extremely controlled environment.
	"""

	q1 = f'''SELECT * FROM {t_name}
		WHERE {col_name} = {where_adlib}
		LIMIT {limit_num}'''
	data = sqlio.read_sql_query(q1, conn)
	print(data)
	return(data.to_json())



@app.route('/pandareaderV1/<filename>')
def pandas_reader(filename = 'stuff'):
	"""
	This version of the pandareader API allows us to select a file from our 
	folder that this code is running from and reading directly into it from 
	pandas. This can also be used to show tables.
	"""

	data = pd.read_csv(filename + '.csv')
	return(data.to_json())



@app.route('/pandareaderV2/<filename>/<col_name>')
def pandas_reader_2(filename = 'stuff', col_name = 'movie'):
	"""
	This is similar to the "old" pandas api and allows us to pick a specific 
	column name to return, and it is just another quick example of us being 
	able to pick out the place that we want to pick up data from, then "clean" 
	it up in some way, and then sending only 1 column back.
	"""

	data = pd.read_csv(filename + '.csv')
	return(data[col_name].to_json())


@app.route('/NextPageSimulator/<inp_num>')
def next_simulator(inp_num):
	"""
	This allows us to type in a page number and click through to skip pages 
	two by two. This is a horrible example of a dynamic page structure, but 
	one nonetheless. We've all been to some part of a website that lands you 
	at a massively long chain of pages that you can click through (either a 
	long list of items to buy, a list of posts, etc.)
	"""

	print(f"The input number is {inp_num}")
	iteratednum = int(inp_num) + 2
	print(f"The iterated number is {iteratednum}")

	"""
	Here the code is autofilling the next link each time iteratednum is 
	created. This is acting in almost a recursive way.
	"""

	if iteratednum > 25:
		return(f"Hi, you got to the last page, please go to</br>" +\
			"<a href='/NextPageSimulator/1'>Next Page Simulator Page 1</a>")
	else:
		return(f"Hi this is the next page simulator!</br>" +
		"Here, you can skip ahead by 2 every time you click!"


		f"<a href='/NextPageSimulator/{iteratednum}''>Next Page Simulator Page {iteratednum}</a>")


if __name__ == "__main__":
    app.run(debug=True)










































