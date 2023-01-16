import requests
import json
import petl
from unidecode import unidecode

# generate a CSV summary of BOC Valet API Series

# set URL and get data
url = 'https://www.bankofcanada.ca/valet/lists/series'
BOCResponse = requests.get(url)
BOCRaw = json.loads(unidecode(BOCResponse.text))

# set up arrays for petl 
series = []
label = []
description = []
link = []

# populate arrays
for seriesDesc in BOCRaw['series']:
	series.append(seriesDesc)
	label.append(BOCRaw['series'][seriesDesc]['label'])
	description.append(BOCRaw['series'][seriesDesc]['description'])
	link.append(BOCRaw['series'][seriesDesc]['link'])

# build petl table and generate CSV
seriesOutput = petl.fromcolumns([series,label,description,link])
petl.tocsv(seriesOutput,'series.csv')
