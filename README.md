# BOCDemo
 
This repository contains Python scripts for use with the Bank of Canada Valet API.

## Dependencies
The following Python modules are required by this solution:

* requests
* matplotlib
* petl
* argparse
* unidecode

## get_series.py

This script generates a CSV (sample included in repository) listing all of the series available through the Valet API.

## factotum.py

**usage: factotum.py [-h] [--start START] [--end END] series filename**
This script generates a chart image from the Valet data series specified on the command line, with a time period optionally specified. Factotum accepts the following command-line arguments:

* **--start** this optional parameter identifies the start date for the data series in the format YYYY-MM-DD
* **--end** this optional parameter identifies the end date for the data series in the format YYYY-MM-DD
* **series** this *required* parameter identifies the series to retrieve data for
* **filename** this *required* parameter identifies the output filename

### Example

The command-line below will generate a chart showing the value of the Bank of Canada's US Dollar holdings in 2022
python factotum.py --start 2022-01-01 --end 2022-12-31 V15943317 USDollars2022.png