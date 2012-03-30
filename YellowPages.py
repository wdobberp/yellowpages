#!/usr/bin/python

import sys
import simplejson, urllib

API_KEY = '19dce8fb6a2df9fbcc5832b95a9e28b4'

SAMPLE_URL = 'http://api2.yp.com/listings/v1/search?term=restaurant&searchloc=Southborough%2BMA&format=JSON&sort=name&listingcount=50&radius=15&useragent=mozilla&key=19dce8fb6a2df9fbcc5832b95a9e28b4'
BASE_URL = 'http://api2.yp.com/listings/v1/search?term='



def sendRequest(searchParam, townParam, radiusParam, pageParam):
	
	URLString = BASE_URL + searchParam + "&searchloc=" + townParam + \
	"%2BMA&format=JSON&sort=name&listingcount=50&radius=" + radiusParam + \
	"&useragent=mozilla&key=19dce8fb6a2df9fbcc5832b95a9e28b4" + \
	"&pageNum=" + str(pageParam) 
	
	result = simplejson.load(urllib.urlopen(URLString))
	searchResults = result['searchResult']
	searchListings = searchResults['searchListings']
	objs = searchListings['searchListing']
	
    # loop thru array of listings
	for obj in objs:
		businessName = obj['businessName']
		email = obj['email']
		street = obj['street']
		phone = obj['phone']
		city = obj['city']
		zip = obj['zip']
		
		print businessName
		print phone
		print street
		print city + ", MA" + " " + zip
		print
		
if (len(sys.argv) > 3):
	keyword = sys.argv[1]
	town = sys.argv[2]
	radius = sys.argv[3]
else:
	print "Usage: <scriptname> keyword town radius"
	print "Example python YellowPages.py Southborough Restaurant 15"
	exit(0)	
	
try:
	page = 1
	while (1):	
		sendRequest(keyword, town, radius, page)
		page = page + 1
finally:
	exit(0)
