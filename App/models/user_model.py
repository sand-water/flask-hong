from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models.model_util import BaseModel


class Users(db.Model,BaseModel):
    u_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    u_name = db.Column(db.String(16),unique=True)

    _u_password=db.Column(db.String(256))

    u_permission=db.Column(db.Integer,default=1)

    @property
    def u_password(self):
        return self._u_password

    @u_password.setter
    def u_password(self,password):
        self._u_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self._u_password,password)

