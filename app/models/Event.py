from system.core.model import *

class Event(Model):
	def __init__(self):
		super(Event, self).__init__()


	def getAllEvents(self):
		query = "SELECT * FROM events"
		return self.db.query_db(query)


	#Get all data about an event.
  	def getEventData(self, event_id):
		query = "SELECT * FROM events WHERE events.id = :event_id"
		data = { "event_id": event_id }
		return self.db.query_db(query, data)


	def getLocationEvent(self, place_id):
		query = "SELECT *, events.id AS event_id FROM events JOIN users ON users.id = events.owner_id WHERE events.location_id = :place_id"
		data = { "place_id": place_id }
		return self.db.query_db(query, data)


	def getUserEvents(self, user_id):
		query = "SELECT users.*, events.*, events.id AS event_id, locations.name AS location_name FROM events JOIN user_events ON events.id = user_events.event_id JOIN users ON users.id = user_events.user_id JOIN locations ON locations.id = events.location_id WHERE user_events.user_id = :user_id"
		data = { "user_id": user_id }
		return self.db.query_db(query, data)


	def getEventUsers(self, event_id):
		query = "SELECT users.* FROM users JOIN user_events ON users.id = user_events.user_id WHERE user_events.event_id = :event_id"
		data = {"event_id": event_id}
		return self.db.query_db(query, data)


	def addUserToEvent(self, event_id, user_id):
		query = "SELECT users.id FROM users JOIN user_events ON users.id = user_events.user_id WHERE user_events.event_id = :event_id AND user_events.user_id = :user_id"
		data = {"event_id": event_id, "user_id": user_id}
		check = self.db.query_db(query, data)

		if len(check) == 0:
			query = "INSERT INTO user_events (user_id, event_id) VALUES (:user_id, :event_id)"
			data = {"event_id": event_id, "user_id": user_id}
			return self.db.query_db(query, data)
		else:
			return []


	#use the google places ID string
	def createEventAtLocation(self, place_id, owner_id, event_name, location_name, description, image_source, eventTime):
		query = "INSERT INTO locations (id, name) VALUES (:place_id, :name) ON DUPLICATE KEY UPDATE id=id"
		data = { "place_id": place_id, "name": location_name}
		self.db.query_db(query, data)
		query = "INSERT INTO events (location_id, owner_id, name, description, image_source, created_at) VALUES (:place_id, :owner_id, :event_name, :eventDesc, :image_source, :eventTime)"
		data = { "place_id": place_id, "owner_id": owner_id, "eventDesc": description, "eventTime": eventTime, "image_source" : image_source, "event_name": event_name }
		event_id = self.db.query_db(query, data)
		query = "INSERT INTO user_events(user_id, event_id) VALUES (:owner_id, :event_id)"
		self.db.query_db(query, { 'owner_id' : owner_id, 'event_id' : event_id })
		self.addUserToEvent(event_id, owner_id)
		return event_id


	def deleteEvent(self, event_id):
		query = 'DELETE FROM events WHERE id=:event_id'
		data = { 'event_id': event_id}
		return self.db.query_db(query, data)


	def showTopfive(self):

		query = "SELECT *, id AS event_id FROM events LIMIT 5"

		return self.db.query_db(query)

