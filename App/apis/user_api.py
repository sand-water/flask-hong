from flask import request
from flask_restful import Resource, fields, marshal_with

from App.models.user_model import Users


user_fields = {
    "id": fields.Integer(attribute="u_id"),
    "name": fields.String(attribute="u_name")
}


user_resource_fields_get = {
    "status": fields.Integer,
    "msg": fields.String(default="ok"),
    "data": fields.Nested(user_fields)
}


class UserResource(Resource):

    @marshal_with(user_resource_fields_get)
    def get(self, id):
        print("11")
        user = Users.query.get(id)

        return {"data": user}

    def post(self, id):

        return {"msg": "post single ok"}

    def delete(self, id):

        user = Users.query.get(id)

        if user:

            user.delete()

            return {"msg": "delete ok"}
        else:
            return {"msg": "does not exist"}

    def put(self, id):
        return {"msg": "put single ok"}

    def patch(self, id):
        return {"msg": "patch single ok"}


users_resource_fields_get = {
    "msg": fields.String(default="ok"),
    "status": fields.Integer,
    "data": fields.List(fields.Nested(user_fields))
}


class UsersResource(Resource):

    @marshal_with(users_resource_fields_get)
    def get(self):
        print("222")
        users = Users.query.all()

        return {"msg": "get ok", "data": users}

    def post(self):

        name = request.form.get("name")

        password = request.form.get("password")

        print(name, password)

        user = Users()
        user.u_name = name
        user.u_password = password

        result = user.save()

        if result:

            return {"msg": "post ok"}
        else:

            return {"msg": "save error"}

    def delete(self):
        return {"msg": "delete ok"}

    def put(self):
        return {"msg": "put ok"}

    def patch(self):
        return {"msg": "patch ok"}

