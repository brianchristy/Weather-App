from urllib import response
import requests

API_KEY='c46fd2de8447d818f37cb167c5a6b11c'
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

city=input('Enter a city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"


'''requests
get:- retrieve information
head:-retrieve resource headers
post:-submit data to the server
put:-save an object at the location
delete:-delete the object at the location'''


response=requests.get(request_url)

if response.status_code==200:
    data=response.json()
    weather=data['weather'][0]['description']
    temp=round(data['main']['temp']-273.15,2)

    print("The weather in",city.capitalize(), "is: ",weather)
    print("And the temperature is: ",temp,'°C')

else:
    print(f"Request failed with status code {response.status_code}")