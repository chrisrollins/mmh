from system.core.controller import *

class Events(Controller):
	def __init__(self, action):
		super(Events, self).__init__(action)
		self.load_model('Event')
		self.load_model('Api')
		self.load_model('Location')
		self.load_model('User')


	def index(self, event_id):
		data = self.models['Event'].getEventData(event_id)
		location_name = self.models['Location'].get_place_name(data[0]["location_id"])
		owner_name = self.models['User'].getUserName(data[0]["owner_id"])
		event_users = self.models['Event'].getEventUsersByName(event_id)
		print event_users
		return self.load_view('/events/index.html', data=data[0], location_name=location_name, owner_name=owner_name)


	def createPage(self):
		return self.load_view('/events/create.html')


	def create(self):
		place_id = request.form["place_id"]
		location_name = request.form["place_name"]
		description = request.form["description"]
		eventTime = request.form["date"]
		eventName = request.form["eventName"]
		owner_id = session["id"]
		print owner_id
		image_source = '/static/img/waterfall-03.jpg' # default waterfall image
		event_id = self.models['Event'].createEventAtLocation(place_id, owner_id, eventName, location_name, description, image_source, eventTime)
		return redirect("/events/" + str(event_id))


	def destroy(self, event_id):
		self.models['Event'].deleteEvent(event_id)
		return redirect('/users/profile')


	def display(self):
		activity = self.models['Event'].showTopfive()
		print activity
		return self.load_view('/partials/eventbox.html', events = activity)