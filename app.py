import json
from venv import create
from flask import Flask, jsonify
from flask_restx import Resource
from api import api, userRepository
from serializer.user import user
from models.user import User

app = Flask(__name__)
api.init_app(app)

ns = api.namespace('CRUD', description="CRUD Operations")

@ns.route("/users")
class Users(Resource):
    def get(self):
        userList = userRepository.getAllUsers()
        return jsonify(userList)


@ns.route("/user/<string:cpf>")
class rUser(Resource):
    def get(self, cpf):
        user = userRepository.getUser(cpf)
        return jsonify(user.toDict())

@ns.route("/user")
class rUser(Resource):
    @ns.expect(user)
    @ns.marshal_with(user, 201)
    def post(self):
        createdUser = userRepository.addUser(User(api.payload))
        return createdUser, 201
    
    @ns.expect(user)
    @ns.marshal_with(user, 200)
    def put(self):
        updatedUser = userRepository.updateUser(User(api.payload))
        return updatedUser, 200

    @ns.expect(user)
    def delete(self):
        deletionMessage = userRepository.deleteUser(User(api.payload))
        return deletionMessage, 200

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()