from system.core.controller import *

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)
        self.load_model('Review')

    def index(self):
        return self.load_view('reviews/index.html')

    def select_all(self):
        reviews = self.models['Review'].select_all()
        print("reviews: ", reviews)
        return reviews

    def select_all_html(self):
        reviews = self.select_all()
        return self.load_view('partials/review.html', reviews=reviews)

    def select_all_json(self):
        reviews = self.select_all()
        return jsonify(reviews=reviews)

    def create(self):
        print("create")
        data = request.form
        self.models['Review'].insert(data)
        reviews = self.models['Review'].select_all()
        return self.load_view('partials/review.html', reviews=reviews)

    def delete(self, id):
        self.models['Review'].delete(id)
        return

