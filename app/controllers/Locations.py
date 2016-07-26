from system.core.controller import *

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)
        self.directions_url = "https://maps.googleapis.com/maps/api/directions/json?key="
        self.maps_url = "https://google.com/maps/embed/v1/place?key=" 
        self.weather_url = "http://api.openweathermap.org/data/2.5/weather?appid="
        self.load_model('Api')
        self.load_model('Location')

    # index: displays the location page for location id specified
    def index(self, location_id):
        location = self.models['Location'].select_by_id(location_id)

        if location:
            place = {
               'name_city' : location[0]['name'] + " " + location[0]['city'],
               'lat_lon'   : str(location[0]['lat']) + ", " + str(location[0]['lon'])
            }
            weather_url = self.get_weather_url(place['name_city'])
            return self.load_view('locations/index.html', place=place, weather_url=weather_url)
        else:
            # redirect to profile page if location doesn't exist
            flash("Unknown location", "error")
            return redirect('/profile')

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

    # get_map: use google maps embedded api to return the url for loading partial html
    def get_map_place(self):
        destination = request.form['destination']
        api_key = self.models['Api'].get_api_key('google_maps_embed')
        url = self.maps_url + api_key + "&" + urlencode({'q' : destination })
        return self.load_view("partials/maps.html", url=url)

    def get_map_search(self):
        pass

    # get_weather_url: get the url for the weather app for a specific location
    def get_weather_url(self, place):
        api_key = self.models['Api'].get_api_key('openweathermap')
        url = self.weather_url + api_key + "&units=imperial&" + urlencode({'q' : place })
        return url

