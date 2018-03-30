import urllib.parse
import requests

main_api = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input('What Address: ')
    if address == 'q' or address == 'quit':
        break

    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)

    json_data = requests.get(url).json()

    json_status = json_data['status']
    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])


        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print(formatted_address)
    else:
        print("No address found")