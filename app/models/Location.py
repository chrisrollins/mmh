from system.core.model import *
import re

# data retrieval manipulation for locations data
class Location(Model):
    def __init__(self):
        super(Location, self).__init__()

    # select_by_id: get all info for one location
    # pass in location id 
    # returns one list item of location info for a specific location 
    def select_by_id(self, id):
        query = "SELECT * FROM locations WHERE id=:id"
        return self.db.query_db(query, { 'id' : id })

    # select_all: get all location data
    # returns list
    def select_all(self):
        query = "SELECT * FROM locations"
        return self.db.query_db(query)

    # insert: insert one row into locations table
    # pass in dictionary object with keys: id, name, city, state, lat, lon
    def insert(self, data):
        print(data)
        query = "INSERT INTO locations (id, name, city, state, lat, lon, created_at, updated_at) \
            VALUES (:id, :name, :city, :state, :lat, :lon, NOW(), NOW())"
        return self.db.query_db(query, data)

    # update: update one row in locations
    # pass in dictionary object with keys: id, name, city, state, lat, lon
    def update(self, data):
        query = "UPDATE locations SET name=:name, city=:city, lat=:lat, lon=:lon, updated_at=NOW() \
            WHERE id=:id"
        return self.db.query_db(query, data)

    # delete: delete one from from locations
    # pass in location id
    def delete(self, id):
        query = "DELETE FROM locations where id=:id"
        return self.db.query_db(query, { 'id' : id })


