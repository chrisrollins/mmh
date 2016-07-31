from system.core.controller import *

class Reviews(Controller):
	def __init__(self, action):
		super(Reviews, self).__init__(action)
		self.load_model('Review')

	def index(self):
		return self.load_view('reviews/index.html')

	def select_all_html(self):
		reviews = self.models['Review'].select_all()
		return self.load_view('partials/review.html', reviews=reviews)

	def select_all_json(self):
		reviews = self.models['Review'].select_all()
		return jsonify(reviews=reviews)

	def create_for_location(self):
		data = request.form
		self.models['Review'].insert(data)
		reviews = self.models['Review'].reviews_by_location(data['location_id'])
		return self.load_view('/partials/reviews.html', reviews=reviews, by_location=data['location_id'])

	# delete a review and return location id or user id for ajax call
	def delete(self, review_id):
		self.models['Review'].delete(review_id)
		if 'by_location' in request.form:
			reviews = self.models['Review'].reviews_by_location(request.form['by_location'])
			return self.load_view('/partials/reviews.html', reviews=reviews, by_location=request.form['by_location'])
		elif 'by_user' in request.form:
			reviews = self.models['Review'].reviews_for_user(request.form['by_user'])
			return self.load_view('/partials/reviews.html', reviews=reviews, by_user=request.form['by_user'])


