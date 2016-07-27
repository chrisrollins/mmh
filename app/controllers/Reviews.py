from system.core.controller import *

class Reviews(Controller):
	def __init__(self, action):
		super(Reviews, self).__init__(action)
		self.load_model('Review')

	def index(self):
		return self.load_view('reviews/index.html')

	def reviews_by_location_html(self, place_id):
		reviews = self.models['Review'].reviews_by_location(place_id)
		return self.load_view('partials/location_reviews.html', reviews=reviews)

	def select_all_html(self):
		reviews = self.models['Review'].select_all()
		return self.load_view('partials/review.html', reviews=reviews)

	def select_all_json(self):
		reviews = self.models['Review'].select_all()
		return jsonify(reviews=reviews)

	def create_for_location(self):
		print("create")
		data = request.form
		self.models['Review'].insert(data)
		reviews = self.models['Review'].reviews_by_location(place_id)
		return self.load_view('partials/location_reviews.html', reviews=reviews)

	def delete(self, id):
		self.models['Review'].delete(id)
		return True

