from system.core.model import *

class Api(Model):
    def __init__(self):
        super(Api, self).__init__()

    # get_api_key: get the api key for specified app
    # possible names: openweathermap, google_maps_directions, google_maps_embed, trailapi, facebooklogin
    # returns a key of type string
    def get_api_key(self, name):
        query = "SELECT api_key FROM api_keys WHERE name = :name";
        result = self.db.query_db(query, { 'name' : name })
        return result[0]['api_key'] if result else ''

