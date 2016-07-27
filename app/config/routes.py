from system.core.router import routes

routes['default_controller']      = 'Welcome'
routes['/profile']                = 'Users#index'
routes['/logout']                 = 'Users#logout'
routes['/review']                 = 'Reviews#index'
routes['/event/<event_id>']       = 'Events#index'
