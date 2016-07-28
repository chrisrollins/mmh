from system.core.controller import *

class Events(Controller):
	def __init__(self, action):
		super(Events, self).__init__(action)
		self.load_model('Event')
		self.load_model('Api')
		self.load_model('Location')


	def index(self, event_id):
		data = self.models['Event'].getEventData(event_id)
		print data
		return self.load_view('/events/index.html', data=data)


	def createPage(self):
		return self.load_view('/events/create.html')


	def create(self):
		place_id = request.form["place_id"]
		location_name = request.form["place_name"]
		description = request.form["description"]
		eventTime = request.form["date"]
		eventName = request.form["eventName"]
		owner_id = session["id"]

		event_id = self.models['Event'].createEventAtLocation(place_id, owner_id, eventName, location_name, description, eventTime)
		return redirect("/events/" + str(event_id))
