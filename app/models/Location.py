from system.core.model import *
import re
import requests
import json

# for python3 a bit kludgey
try:
	from urllib.parse import urlencode #, urlparse
except ImportError:
	from urllib import urlencode

# data retrieval manipulation for locations data
class Location(Model):
	def __init__(self):
		super(Location, self).__init__()
		self.directions_url = "https://maps.googleapis.com/maps/api/directions/json?key="
		self.place_url = "https://maps.googleapis.com/maps/api/place/details/json?key="
		self.maps_url = "https://google.com/maps/embed/v1/place?key=" 
		self.weather_url = "http://api.openweathermap.org/data/2.5/weather?appid="

	# get_place_info: get detail location information given a place id
	# return a json response
	def get_place_info(self, place_id):
		api_key = self.get_api_key('google_maps_directions')
		url = self.place_url + api_key + "&placeid=" + place_id
		response = requests.get(url).content
		return response

	# get_place_info_obj: call get_place_info to convert json string
	# json.loads() unserializes json string
	# return dictionary object
	def get_place_info_obj(self, place_id):
		json_str = self.get_place_info(place_id)
		return json.loads(json_str)

	# get_place_name: given a place_id return the location name
	def get_place_name(self, place_id):
		query = "SELECT name FROM locations WHERE id = :id "
		row = self.db.query_db(query, { 'id' : place_id })
		return row[0]['name'] if row else ''

	# get_weather: get weather information for a given place id
	# return a json response
	def get_weather(self, place_id):
		location_info = self.get_place_info_obj(place_id)
		lat = location_info['result']['geometry']['location']['lat']
		lon = location_info['result']['geometry']['location']['lng']

		api_key = self.get_api_key('openweathermap')
		url = self.weather_url + api_key + "&units=imperial&" + urlencode({ 'lat' : lat, 'lon' : lon })
		response = requests.get(url).content
		return response

	# get_weather_obj: call get_weather to convert json string
	# return dictionary object
	def get_weather_obj(self, place_id):
		json_str = self.get_weather(place_id)
		return json.loads(json_str)

	# get_directions: use google maps directions api to get directions
	# from origin to destination
	def get_directions(self):
		data = {
			'origin'      : request.form.get('from', ''),
			'destination' : request.form.get('to', '')
		}
		api_key = self.get_api_key('google_maps_directions')
		url = self.directions_url + api_key + "&sensor=false" + "&" + urlencode(data)
		response = requests.get(url).content
		return response

	# get_api_key: get the api key for specified app
	# possible names: openweathermap, google_maps_directions, google_maps_embed, trailapi, facebooklogin
	# returns a key of type string
	def get_api_key(self, name):
		query = "SELECT api_key FROM api_keys WHERE name = :name";
		result = self.db.query_db(query, { 'name' : name })
		return result[0]['api_key'] if result else ''
