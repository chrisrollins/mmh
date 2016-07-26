from system.core.controller import *

class Events(Controller):
    def __init__(self, action):
        super(Events, self).__init__(action)
        self.load_model('Event')
        self.load_model('Api')
        self.load_model('Location')

    def index(self):
        return self.load_view('/events/index.html')

