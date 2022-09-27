from requests import get

ip = get('https://api.ipify.org/').text
# ip = '79.132.124.85'
url = f'http://ip-api.com/json/{ip}'
req = get(url=url).json()
location = f"{req['lat']}, {req['lon']}"
print(location)

###############################################################

from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
from requests import exceptions, get

# location = [54.3205, 48.4468]
geoloc = Nominatim(user_agent='GetLoc')
locname = geoloc.reverse(location)
print(locname.address)

##############################################################
