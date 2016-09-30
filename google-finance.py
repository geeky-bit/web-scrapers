"""
Scrape FTSE100 Historical Prices from Google Finance

Author: Jessica Yung
September 2016
"""

from bs4 import BeautifulSoup
import urllib.request
# from sys import argv
import re
import math

# script, theurl = argv

def append_page_figures(url):
	html = urllib.request.urlopen(url).read()	
	soup = BeautifulSoup(html, "lxml")
	# Select element with class `historical_price`
	historical_prices = soup.select(".historical_price")

	# For each tr, create new row then 
	# append values of each td to that row except the td with class rm. 

	# rows = all tr
	# Rows is type <class 'bs4.element.ResultSet'>
	# historical_prices is a list of length 1 since 1 el selected
	rows = historical_prices[0].find_all('tr')
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
			if value[0].isdigit():
				value = float(value.replace(',',''))
			row_data.append(value)
		# Take away the dash for volume
		row_data = row_data[:-1]
#		print(row_data)
		stock_data.append(row_data)

def number_of_pages():
	"""Returns tho number of pages you need to scrape to get all the
	data for this security in your date range."""
	# Max rows_per_page = 200
	total_pages = math.ceil(total_rows/rows_per_page)
	return total_pages

def assemble_stock_query(start):
	"""Returns the URL for a page for your security (and parameters such
	and start and end dates) with the first row in the table being 
	row `start` (int)."""
	query = gfinance_url
	for key, value in q.items():
		to_append = str(key) + "=" + str(value) + "&"
		query += to_append
	# TODO: Check syntax of code in the line below
	query += "start=%s" % str(start)
	return query

def write_to_file(data, filename, header=None):
	with open(filename, "a") as f:
		if header != None:
			f.write(str(header)[1:-1])
			f.write("\n")
		for row in stock_data:
			f.write(str(row)[1:-1])
			f.write("\n")

# Initialise Variables
gfinance_url = "https://www.google.co.uk/finance/historical?"
total_rows = 40
rows_per_page = 20	
q = {
	"cid": "12590587",
	"startdate": "Jan+1%2C+1977",
	"enddate": "Sep+9%2C+2016",
	"num": rows_per_page,
	"ei": "iIXuV9HQFJfEU42QtNgD"	
}
stock_data = []
header = ["Date", "Open", "High", "Low", "Close"]
filename = "ftse100.csv"
# Get URL for each page, scrape data from each page and 
# append scraped data to `stock_data`.
for page_index in range(number_of_pages()):
	start = page_index * rows_per_page
	new_url = assemble_stock_query(start)
	append_page_figures(new_url)

# Print head and tail of `stock_data` to check it is correct
print(stock_data[:20])
print(stock_data[-20:])

write_to_file(stock_data, filename, header=header)

# Write data to file

# Add header row

# Add other rows

# Sample URLs:
# https://www.google.co.uk/finance/historical?cid=12590587&startdate=Jan+1%2C+1977&enddate=Sep+9%2C+2016&num=200&ei=iIXuV9HQFJfEU42QtNgD&start=200
# https://www.google.co.uk/finance/historical?cid=12590587&startdate=Jan%201%2C%201977&enddate=Sep%209%2C%202016&num=200&ei=9IfuV4jzOtfJUaSJjrgG&start=200
