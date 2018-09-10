from flask_restful import Api


from App.apis.user_api import UserResource, UsersResource

api = Api()


def init_api(app):
    api.init_app(app=app)



api.add_resource(UsersResource, "/users/")
api.add_resource(UserResource, "/users/<int:id>/")

