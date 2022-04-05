import requests

#  	        NO2 	PM10 	O3    	PM25 (optional)
# Good 	 	0-50 	0-25 	0-60 	    0-15
# Fair 	 	50-100 	25-50 	60-120 	    15-30
# Moderate 	100-200 50-90 	120-180 	30-55
# Poor  	200-400 90-180 	180-240 	55-110
# Very Poor	>400 	>180 	>240 	    >110

api_key = "a3708191b122f6cc2c2d8da08b9f5737"
NO2 = 0
PM10 = 0
O3 = 0
PM25 = 0

def getPollut(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url).json()
    NO2 = response['list'][0]['components']['no2']
    PM10 = response['list'][0]['components']['pm10']
    O3 = response['list'][0]['components']['o3']
    PM25 = response['list'][0]['components']['pm2_5']

    print("Microgram per cubic meter")
    print(f"NO2:{NO2}μg/m3  |   PM10:{PM10}μg/m3    |    O3:{O3}μg/m3   |   PM25:{PM25}μg/m3")
    aqi = response['list'][0]['main']['aqi']
    return aqi

lat = input("Enter your lattitude: ")
lon = input("Enter your longitude: ")

aqi = getPollut(api_key, lat, lon)

if aqi == 1:
    print("Air Quality: Good")
if aqi == 2:
    print("Air Quality: Fair")
if aqi == 3:
    print("Air Quality: Moderate")
if aqi == 4:
    print("Air Quality: Poor")
if aqi == 5:
    print("Air Quality: Very Poor")