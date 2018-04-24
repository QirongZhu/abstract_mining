import requests
import urllib
my_token = 'Copy your token from your ADS account'
query = urllib.quote_plus('full:"black holes" bibstem:"MNRAS" year:2016')
fields = urllib.quote_plus("bibcode,pubdate")
r = requests.get("https://ui.adsabs.harvard.edu/v1/search/query?q={0}&fl={1}&rows=0".format(query, fields), headers={'Authorization': 'Bearer ' + my_token},)
numFound = r.json()['response']['numFound']
results = r.json()['response']['docs']
print(numFound)
