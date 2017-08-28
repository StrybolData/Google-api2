
import googlemaps
import json
from datetime import datetime

gmaps = googlemaps.Client(key='put your key here')

list_of_addresses_in =[("13 Stutfield St, Whitechapel, London E1, United Kingdom"), ("59 Brady St, London E1, United Kingdom"), ("83 Nelson St, Whitechapel, London E1 2HN, United Kingdom"), ("46 Portelet Rd, London E1 4EJ, United Kingdom"),("165-203 Hanbury St, London E1 5HZ, United Kingdom")]

for i in range(len(list_of_addresses_in)-1):
    direction_result = gmaps.directions(list_of_addresses_in[i], list_of_addresses_in[i+1], mode='transit', departure_time=datetime.now())
#direction_result = gmaps.directions("Zeelaan 50 8400 Oostende Belgium", "Middenlaand 13 8400 Oostende Belgium", mode='transit', departure_time=datetime.now())
distance_result = direction_result[0]['legs'][0]['distance']['value']
print('Total distance of the route:', distance_result)

#print(distance_result)
#data_json= json.dumps(direction_result, indent= 4)
#print(data_json)
