from system.core.router import routes

routes['default_controller']      = 'Welcome'
routes['/location/<location_id>'] = 'Locations#index'
routes['/profile']                = 'Users#index'
routes['/logout']                 = 'Users#logout'
routes['/review']                 = 'Reviews#index'
routes['/event']                  = 'Events#index'
