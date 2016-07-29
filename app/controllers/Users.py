from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.load_model('Review')
		self.load_model('Api')
		self.load_model('Event')
		self.load_model('Location')

	def index(self):
		return self.load_view('/users/index.html')

	# logout: clears session
	# logs out of facebook?
	def logout(self):
		
		print "THS IS THE SECOND accessTOKEN!"
		print session['accessToken']
		url = 'https://www.facebook.com/logout.php?next=http://52.42.107.10/&access_token={}'.format(session['accessToken'])
		print url
		session.clear()
		return jsonify({"status": True})

	def create(self):
		data = {
			'handle': request.form['handle'],
			'id': request.form['id'],
			'email': request.form['email'],
		}


		session['accessToken'] = request.form['token']
		print "this is the acces Token:"
		print session['accessToken']	 

		user = self.models['User'].create(data)
		session['id'] = user 
	

		return redirect('/users/profile')

	def profile(self):
		return self.load_view('/users/profile.html')

	def get_events_for_user(self):
		
		events = self.models['Event'].getUserEvents(session['id'])

		print events
		return self.load_view('/partials/eventbox.html', events=events)

	def get_reviews_for_user(self):
		reviews = self.models['Review'].reviews_for_user(session['id'])
		return self.load_view('/partials/user_reviews.html', reviews=reviews)



