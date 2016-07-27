from system.core.model import *

class Review(Model):
	def __init__(self):
		super(Review, self).__init__()

	def reviews_by_location(self, place_id):
		query = "SELECT * FROM reviews WHERE location_id = :id ORDER BY updated_at DESC"
		return self.db.query_db(query, { 'id' : place_id })
		
	def select_all(self):
		query = "SELECT * FROM reviews ORDER BY updated_at DESC"
		return self.db.query_db(query)

	def insert(self, data):
		query = "INSERT INTO reviews (location_id, user_id, review, created_at, updated_at) \
			VALUES (:location_id, :user_id, :review, NOW(), NOW())"
		return self.db.query_db(query, data)

	def delete(self, id):
		query = "DELETE FROM reviews WHERE id=:id"
		return self.db.query_db(query, { 'id' : id })

