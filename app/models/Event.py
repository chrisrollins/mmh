from system.core.model import *

class Event(Model):
    def __init__(self):
        super(Event, self).__init__()


    def getAllEvents(self):
    	query = "SELECT * FROM events"
        return self.db.query_db(query)


    #Get all data about an event.
  	def getEventData(self, event_id):
    	query = "SELECT * FROM events WHERE events.id = event_id"
        data = { "event_id": event_id }
        return self.db.query_db(query)


    def getLocationEvent(self, place_id):
    	query = "SELECT * FROM events JOIN users ON users.id = events.owner_id WHERE events.location_id = :place_id"
        data = { "place_id": place_id }
        return self.db.query_db(query, data)


    def getUserEvents(self, user_id):
    	query = "SELECT * FROM events JOIN user_events ON events.id = user_events.event_id JOIN users ON users.id = user_events.user_id WHERE user_events.user_id = :user_id"
        data = { "user_id": user_id }
        return self.db.query_db(query, data)


    #use the google places ID string
    def createEventAtLocation(self, place_id, owner_id, location_id, description, eventTime, ):
    	query = "INSERT INTO events (name, description, location_id, owner_id, created_at) VALUES (:eventName, :eventDesc, :loc, :owner, :eventTime)"
        data = { "user_id": user_id }
        return self.db.query_db(query, data)