from database import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.INT, primary_key=True)
    username = db.Column(db.TEXT, nullable=False)

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def __str__(self):
        return f"User: id={self.id}, username={self.username}"