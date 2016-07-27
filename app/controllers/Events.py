from system.core.controller import *

class Events(Controller):
	def __init__(self, action):
		super(Events, self).__init__(action)
		self.load_model('Event')
		self.load_model('Api')
		self.load_model('Location')


	def index(self, id):
		locationName = self.models('Location').getLocationName(id) #??
		location_id = self.models('Event').getEventLocationID(id)
		ownerName = self.models('Event').getOwnerID(id)
		date = self.models('Event').getDate(id)
		time = self.models('Event').getTime(id)
		return self.load_view('/events/index.html', locationName=locationName, location_id=location_id, ownerName=ownerName, date=date, time=time)


	def createPage(self):
		return self.load_view('/events/create.html')


	def create(self):
		return self.load_view('/events/create.html')
