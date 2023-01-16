import requests
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
import argparse
import json

dimensions = []
values = []

parser = argparse.ArgumentParser(description='Generate graphs from Bank of Canada series observations')
parser.add_argument ('series')
parser.add_argument ('--start')
parser.add_argument ('--end')
parser.add_argument ('filename')
args = parser.parse_args()

print('Processing ' + args.series)

url = 'https://www.bankofcanada.ca/valet/observations/' + args.series + '/json'
query = '?'
if (args.start != None):
	query +='start_date=' + args.start
if (args.end != None):
	if len(query) > 1:
		query +='&'
	query +='end_date=' + args.end

print (url + query)

BOCResponse = requests.get(url + query)
seriesDescription = json.loads(BOCResponse.text)['seriesDetail'][args.series]['description']
observations = json.loads(BOCResponse.text)['observations']

for observation in observations:
	dimension = observation['d']
	value = float(observation[args.series]['v'])
	dimensions.append(dimension)
	values.append(value)

pyplot.rcParams.update({'font.size':6})

fig, ax = pyplot.subplots()
ax.tick_params(axis='x',rotation=50)
ax.set(xlabel = 'date',ylabel = args.series)
ax.xaxis.set_major_locator(pyplot.MaxNLocator(25))
ax.yaxis.set_major_locator(pyplot.MaxNLocator(20))
ax.set_title(seriesDescription,loc='center',wrap=True)
ax.plot (dimensions, values)
ax.grid()
fig.savefig(args.filename)

print (dimensions,values)