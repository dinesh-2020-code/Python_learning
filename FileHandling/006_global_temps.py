"""
    Streams:
        -> In today's connected world, data no longer has to exist on your local file system.
        -> It could come from another computer on your network, or from the internet, It's increasingly common for data
        to be stored on remote servers, or in the "cloud".
        -> A long long time ago, the designers of languages like 'C', worked with 'streams'.
        -> When reading from a text file, we actually use a text stream. When getting data from teh keyboard, C uses an
        input stream.
        -> We read from a stream that's connected to an input source, and write to a stream that's connected to an
        output destination. By associating our text streams to a different input or output, we can get data from
        (or send data to) different places, without making huge changes to our code.

"""

import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/3/1850-2024/data.json'

# with open(json_data_source, encoding='utf-8') as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.load(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year}...{value:6.2f}')

print("*" * 72)

# print(anomalies['citation'])
