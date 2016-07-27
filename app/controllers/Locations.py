from system.core.controller import *
import json

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)
        self.directions_url = "https://maps.googleapis.com/maps/api/directions/json?key="
        self.place_url = "https://maps.googleapis.com/maps/api/place/details/json?key="
        self.maps_url = "https://google.com/maps/embed/v1/place?key=" 
        self.weather_url = "http://api.openweathermap.org/data/2.5/weather?appid="
        self.load_model('Api')
        self.load_model('Location')

    # index: displays the location page for location id specified
    def index(self, place_id):
        #place_id = 'ChIJ-ZogKrvMj4ARKrML-5D1a88'
        location_info = self.get_place_info_obj(place_id)
        if location_info['status'] == "OK":
            name = location_info['result']['name']
            return self.load_view('locations/index.html', location_name=name, place_id=place_id)
        else:
            # redirect to profile page if location doesn't exist
            flash("Unknown location", "error")
            return redirect('/profile')

    # get_map: use google maps embedded api to get map
    # load partial html
    def get_map_html(self, place_id):
        api_key = self.models['Api'].get_api_key('google_maps_embed')
        destination = "place_id:" + place_id
        url = self.maps_url + api_key + "&" + urlencode({'q' : destination })
        return self.load_view("partials/maps.html", url=url)

    # get_place_info: get detail location information given a place id
    # return a json response
    def get_place_info(self, place_id):
        api_key = self.models['Api'].get_api_key('google_maps_directions')
        url = self.place_url + api_key + "&placeid=" + place_id
        response = requests.get(url).content
        return response

    # get_place_info_obj: call get_place_info to convert json string
    # json.loads() unserializes json string
    # return dictionary object
    def get_place_info_obj(self, place_id):
        json_str = self.get_place_info(place_id)
        return json.loads(json_str)

    # get_weather: get weather information for a given place id
    # return a json response
    def get_weather(self, place_id):
        location_info = self.get_place_info_obj(place_id)
        lat = location_info['result']['geometry']['location']['lat']
        lon = location_info['result']['geometry']['location']['lng']

        api_key = self.models['Api'].get_api_key('openweathermap')
        url = self.weather_url + api_key + "&units=imperial&" + urlencode({ 'lat' : lat, 'lon' : lon })
        response = requests.get(url).content
        return response

    # get_weather_obj: call get_weather to convert json string
    # return dictionary object
    def get_weather_obj(self, place_id):
        json_str = self.get_weather(place_id)
        return json.loads(json_str)

    # get_weather_html: gets weather info
    # return partial html
    def get_weather_html(self, place_id):
        weather = self.get_weather_obj(place_id)
        return self.load_view('partials/weather.html', weather=weather)

    # get_directions: use google maps directions api to get directions
    # from origin to destination
    def get_directions(self):
        data = { 
            'origin'      : request.form.get('from', ''), 
            'destination' : request.form.get('to', '') 
       }
        api_key = self.models['Api'].get_api_key('google_maps_directions')
        url = self.directions_url + api_key + "&sensor=false" + "&" + urlencode(data)
        response = requests.get(url).content
        return response

