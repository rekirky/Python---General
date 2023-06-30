import requests 

print(f"Getting your IP address")
ipAdd = requests.get("https://api.ipify.org").text
url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
geo_requests = requests.get(url)
geo_data = geo_requests.json()
print(f"Getting your Geolocation")
city =  geo_data['city']
country = geo_data['country']
print(f"You are most likely in {city}, {country}")
