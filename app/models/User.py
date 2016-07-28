from system.core.model import *

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create(self,info):
		query = "INSERT INTO users (id, handle, email, created_at, updated_at) VALUES (:id, :handle, :email, NOW(), NOW())"
		data = {
			'id': info['id'],
			'handle': info['handle'],
			'email': info['email']
		}
		print 'inserting data'

		check_query = "SELECT * FROM users WHERE id = :id "
		check_id = { 'id':info['id']}
		check_user = self.db.query_db(check_query,check_id)

		if check_user:
			return check_user[0]['id']
		else:
			self.db.query_db(query,data)
			get_user = "SELECT users.id FROM users ORDER BY id DESC LIMIT 1"
			return self.db.query_db(get_user)

		
	
