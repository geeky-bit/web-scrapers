"""
Scrape FTSE100 Historical Prices

Author: Jessica Yung
September 2016
"""
from bs4 import BeautifulSoup
import urllib.request
# from sys import argv
import re
import math

# script, theurl = argv

# url with date, stock, start date, end date, number of rows per page (max 200)
url = "https://www.google.co.uk/finance/historical?cid=12590587&startdate=Jan+1%2C+1977&enddate=Sep+9%2C+2016&num=10&ei=iIXuV9HQFJfEU42QtNgD"

# https://www.google.co.uk/finance/historical?cid=12590587&startdate=Jan+1%2C+1977&enddate=Sep+9%2C+2016&num=200&ei=iIXuV9HQFJfEU42QtNgD&start=200
# https://www.google.co.uk/finance/historical?cid=12590587&startdate=Jan%201%2C%201977&enddate=Sep%209%2C%202016&num=200&ei=9IfuV4jzOtfJUaSJjrgG&start=200

def init():
	gfinance_url = "https://www.google.co.uk/finance/historical?"
	q = {
	"cid": "12590587"
	"startdate": "Jan+1%2C+1977"
	"enddate": "Sep+9%2C+2016"
	"num": rows_per_page
	"ei": "iIXuV9HQFJfEU42QtNgD"	
}

def append_page_figures(url):
	# html = urllib.request.urlopen(url).read()
	with open("googlefinance.html", "r") as html:	
		soup = BeautifulSoup(html, "lxml")
		# Select element with class `historical_price`
		historical_prices = soup.select(".historical_price")

		# For each tr, create new row then 
		# append values of each td to that row except the td with class rm. 
	
		# rows = all tr
		# Rows is type <class 'bs4.element.ResultSet'>
		# historical_prices is a list of length 1 since 1 el selected
		rows = historical_prices[0].find_all('tr')
		print(rows)
		print(len(rows))
		# Remove header row
		rows = rows[1:]
		for row in rows:
			cells = row.find_all('td')
			row_data = []
			for cell in cells:
				value = cell.contents
				# Remove it from the len 1 array, 
				# take away the newline character
				value = value[0][:-1]
				print(value)
				row_data.append(value)
			# Take away the dash for volume
			row_data = row_data[:-1]
			print(row_data)
			stock_data.append(row_data)

stock_data = []

def number_of_pages():
	total_rows = 8188
	# Max rows_per_page = 200
	rows_per_page = 200
	total_pages = math.ceil(total_rows/rows_per_page)
	return total_pages

print(number_of_pages())
# append_page_figures(url)

def assemble_stock_query():
	query = ""
	for key, value in q:
		query.append str(key) + "=" + str(value)
		query.append("&")
	# TODO: Check syntax of code in the line below
	query.remove("&")
	return query

query = "cid=" + q["cid"] + "startdate" + q["startdate"]
	# Set query parameters

for i in range
assemble_query()


"""
[<table class="gf-table historical_price">
<tr class="bb">
<th class="bb lm lft">Date
</th><th class="rgt bb">Open
</th><th class="rgt bb">High
</th><th class="rgt bb">Low
</th><th class="rgt bb">Close
</th><th class="rgt bb rm">Volume
</th></tr><tr>
<td class="lm">Sep 9, 2016
</td><td class="rgt">6,858.70
</td><td class="rgt">6,862.38
</td><td class="rgt">6,762.30
</td><td class="rgt">6,776.95
</td><td class="rgt rm">-
</td></tr><tr>


"""
"""
<table class="gf-table historical_price">
if class is NOT equal to bb
copy"""

