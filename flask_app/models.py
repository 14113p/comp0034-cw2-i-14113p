from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flask_app import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    #__table__ = db.Model.metadata.tables["user"]
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return f"{self.id} {self.firstname} {self.lastname} {self.email} {self.password}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

