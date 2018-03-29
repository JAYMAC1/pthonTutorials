import urllib.parse
import requests

main_api = "http://maps.googleapis.com/maps/api/geocode/json?"



while True:
    address = input('What Address: ')
    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)

    json_data = requests.get(url).json()

    json_status = json_data['status']

    print('API Status: {0}'.format(json_status))