from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('Api')
  
    def index(self):
        appId = self.models['Api'].get_api_key('facebooklogin') 
        return self.load_view('index.html', appId=appId)

    def get_navbar(self):
        return self.load_view('partials/navbar.html')
