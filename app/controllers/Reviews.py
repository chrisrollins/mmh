from system.core.controller import *

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)
        self.load_model('Review')

    def index(self):
        return self.load_view('reviews/index.html')
