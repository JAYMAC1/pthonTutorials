import urllib.parse
import requests


# North Ayrshire Council opendata protal (Domestic Waste collection)
api_url = "https://opendata.arcgis.com/datasets/a31ab0fac25e44fe9288b0b9822e02f9_16.geojson"

# Get url contents and convert to json
json_data = requests.get(api_url).json()

# get resedents uprn number "126077891"
UPRN = input("Please enter your UPRN: ")
bin_query = input("Which colour bin are you enquiring about? ")
got_info = []

# iterate through the result
for each in json_data['features']:
    if str(each['properties']['UPRN']) == UPRN:
        got_info = each['properties']
        break

if got_info:
    if(bin_query.upper() == 'BLUE'):
        collection_date = got_info['BLUE_DATE']
    else:
        collection_date = got_info['GREY_DATE']

    collection_day = got_info['BLUE_GREY']
    print('The collection day for your blue or grey bin is the {0} of each week.'.format(collection_day))
    print('The next collection is {0}.'.format(collection_date))
else:
    print("Sorry. No Info")