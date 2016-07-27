from system.core.controller import *

class Locations(Controller):
	def __init__(self, action):
		super(Locations, self).__init__(action)
		self.load_model('Location')
		self.load_model('Event')

	# index: displays the location page for location id specified
	def index(self, place_id):
		location_info = self.models['Location'].get_place_info_obj(place_id)
		if location_info['status'] == "OK":
			name = location_info['result']['name']

			events = self.get_location_events_html(place_id)
			print("events: ", events)

			return self.load_view('locations/index.html', location_name=name, place_id=place_id, user_id=1)
		else:
			# redirect to profile page if location doesn't exist
			flash("Unknown location", "error")
			return redirect('/profile')

	# get_map: use google maps embedded api to get map
	# load partial html
	def get_map_html(self, place_id):
		api_key = self.models['Location'].get_api_key('google_maps_embed')
		destination = "place_id:" + place_id
		maps_url = self.models['Location'].maps_url
		url = maps_url + api_key + "&" + urlencode({'q' : destination })
		return self.load_view("partials/maps.html", url=url)

	def get_place_info_html(self, place_id):
		location_info = self.models['Location'].get_place_info_obj(place_id)
		return self.load_view("partials/location.html", location=location_info['result'])

	# get_weather_html: gets weather info
	# return partial html
	def get_weather_html(self, place_id):
		weather = self.models['Location'].get_weather_obj(place_id)
		return self.load_view('partials/weather.html', weather=weather)

	# get_place_name: given place_id return place name
	def get_place_name(self, place_id):
		return self.models['Location'].get_place_name(place_id)

	def get_location_events_html(self, place_id):
		events = self.models['Event'].getLocationEvent(place_id)

		return events
	

