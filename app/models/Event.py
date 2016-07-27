from system.core.model import *

class Event(Model):
    def __init__(self):
        super(Event, self).__init__()


    def getAllEvents(self):
    	query = "SELECT * FROM events"
        return self.db.query_db(query)


    #Returns the ID of the location the event is at.
    def getEventLocationID(self, event_id):
		query = "SELECT location_id FROM events WHERE events.event_id = :event_id"
        data = { "event_id": event_id }
        return self.db.query_db(query, data)


   	#Returns the user ID of the owner of the event.
    def getOwnerID(self, event_id):
		query = "SELECT owner_id FROM events WHERE events.event_id = :event_id"
        data = { "event_id": event_id }
        return self.db.query_db(query, data)


  	#Returns the day, month, and year the event is scheduled for.
    def getDate(self, event_id):
    	pass


   	#Returns the time the event is scheduled for. (ie. 6:35 PM)
    def getTime(self, event_id):
    	pass


    #Returns the owner's description of the event.
    def getEventDescription(event_id):
		query = "SELECT description FROM events WHERE events.event_id = :event_id"
        data = { "event_id": event_id }
        return self.db.query_db(query, data)


    def getLocationEvent(self, place_id):
    	query = "SELECT * FROM events JOIN users ON users.id = events.owner_id WHERE events.location_id = :place_id"
        data = { "place_id": place_id }
        return self.db.query_db(query, data)


    def getUserEvents(self, user_id):
    	query = "SELECT * FROM events JOIN user_events ON events.id = user_events.event_id JOIN users ON users.id = user_events.user_id WHERE user_events.user_id = :user_id"
        data = { "user_id": user_id }
        return self.db.query_db(query, data)




