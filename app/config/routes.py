from system.core.router import routes

routes['default_controller']      = 'Welcome'
routes['/profile']                = 'Users#index'
routes['/logout']                 = 'Users#logout'
routes['/review']                 = 'Reviews#index'
routes['/event/<event_id>']       = 'Events#index'
routes['/event/new']              = 'Events#createPage' #use to link to the event creation page when the user wants to create a new event
routes['POST']['/event/create']   = 'Events#create' #only used by the event creation page, do not use