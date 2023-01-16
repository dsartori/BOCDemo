import requests
import configparser
import json
import petl
from unidecode import unidecode

url = 'https://www.bankofcanada.ca/valet/lists/series'

BOCResponse = requests.get(url)
BOCRaw = json.loads(unidecode(BOCResponse.text))
series = []
label = []
description = []
link = []

j = 0

for seriesDesc in BOCRaw['series']:
	series.append(seriesDesc)
	label.append(BOCRaw['series'][seriesDesc]['label'])
	description.append(BOCRaw['series'][seriesDesc]['description'])
	link.append(BOCRaw['series'][seriesDesc]['link'])
	
seriesOutput = petl.fromcolumns([series,label,description,link])
petl.tocsv(seriesOutput,'series.csv')
