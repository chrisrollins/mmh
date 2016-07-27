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
        return redirect('/users/profile')

    def profile(self):
        return self.load_view('/users/profile.html')

    def get_events_for_user(self):
        events = self.models['Event'].getUserEvents(session['id'])
        for event in events:
            event['location_name'] = self.models['Location'].get_place_name(event['location_id'])
        return self.load_view('/partials/eventbox.html', events=events)



