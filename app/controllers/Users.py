from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.load_model('Review')
		self.load_model('Api')

	def index(self):
		return self.load_view('/users/index.html')

	# logout: clears session
	# logs out of facebook?
	def logout(self):
		session.clear()
		return redirect('/')

	def create(self):
		data = {
			'handle': request.form['handle'],
			'id': request.form['id'],
			'email': request.form['email']
		}
		print data

		user = self.models['User'].create(data)
		print user['id']
		return redirect('/')

