from system.core.router import routes

routes['default_controller']      = 'Events'
routes['/location/<location_id>'] = 'Locations#index'
routes['/profile']                = 'Users#index'
routes['/logout']                 = 'Users#logout'
routes['/review']                 = 'Reviews#index'
