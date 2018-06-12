import requests # written with requests version 2.18.4
import sys

# The following code retrieves the longitude and latitude of any zipcode and country
# zipcode: a standard numerical or string value for a zipcode
# country: a string value for a country
#
# To run from the command line: 
# In>>: python3 getlonglat.py 8001 'Switzerland'
# Out>>: Latitude:  47.3741561, Longitude:  8.5396323
#
# There are restrictions of 2,500 free requests per day to the geocoding googleapi
# More information about usage limits are here:
# https://developers.google.com/maps/documentation/geocoding/usage-limits

def f(zipcode, country):
###################################################################################
    wiki = 'https://maps.googleapis.com/maps/api/geocode/json'
    apiKey = #put your personal google API Key here
    # Utilize these websites to get your own credentials
    # Be sure to give your apiKey access to the geocoding api
###################################################################################
    params = {'address': str(zipcode) + ' ' + country, 'key': apiKey}
    # requests pings maps.googleapis.com and retrieves the JSON file amongst other things
    # The requests library sends HTTP/1.1 requests in Python.
    r = requests.get(url=wiki, params=params)

# We try pinging the geocoding googleapi, and we return a status message is this fails
    while True:
        try:
            results = r.json()['results']
            # results[0] is a python dictionary stored in the JSON file with lots of information
            # In>>: results[0].keys()
            # Out>>: dict_keys(['address_components', 'types', 'formatted_address', 'place_id', 'geometry'])
            location = results[0]['geometry']['location']
            # location is now another dictionary containing an approximated longitude and latitude
            # In>>: location
            # Out>>: {'lat': 47.3741561, 'lng': 8.5396323} #for these numbers, we used zipcode=8001 and country=Switzerland
            return location['lat'], location['lng']
        # We send an error message in case there are any errors.
        # More information can be found:
        # https://developers.google.com/maps/documentation/geocoding/intro#StatusCodes
        except:
            status = r.json()['status']
            dic = {
                "OK": 'indicates that no errors occurred; the address was successfully parsed and at least one geocode was returned.',
                "ZERO_RESULTS": 'indicates that the geocode was successful but returned no results.\
                This may occur if the geocoder was passed a non-existent address.',
                "OVER_QUERY_LIMIT": 'indicates that you are over your quota.',
                "REQUEST_DENIED": 'indicates that your request was denied.',
                "INVALID_REQUEST": 'generally indicates that the query (address, components or latlng) is missing.',
                "UNKNOWN_ERROR": 'indicates that the request could not be processed due to a server error. \
                The request may succeed if you try again.'
                }
            print('Status message, '+status+': '+dic[status])
            return 0,0

if __name__=='__main__':
    latitude, longitude = f(sys.argv[1], sys.argv[2])
    print('Latitude: %10f, Longitude: %10f' % (latitude, longitude))
