import requests
class weather:
	def __init__(self):
		self.url = 'http://api.openweathermap.org/data/2.5/weather'
		self.api_key = '3489183fc50229f2729d6b8912efdd42'

	def get_weather(self,lat,lon):
		weather_feature = None
		req = requests.get(self.url+'?lat='+str(lat)+"&lon="+str(lon)+"&appid="+self.api_key)
		weather_id =  int(req.json()['weather'][0]['id'])
		print "Fetched weather id",weather_id
		if 200 <= weather_id <= 540:
			weather_feature = 'rainy'
		elif 600 <= weather_id <= 622:
			weather_feature = 'snowy'
		elif weather_id == 701 or weather_id == 711 or weather_id == 721 or weather_id == 741:
			weather_feature = 'cloudy'
		elif weather_id == 800:
			weather_feature = 'sunny'
		elif 801 <= weather_id <= 804:
			weather_feature = 'cloudy'
		elif 951 <= weather_id <= 954:
			weather_feature = 'breezy'
		elif 955 <= weather_id <= 959:
			weather_feature = 'windy'
		else:
			weather_feature = 'sunny'
		return weather_feature
