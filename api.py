from flask import jsonify
from flask_restx import Api
from repositories.usersRepository import UserRepository


userRepository = UserRepository("Simpleflaskapi_serviceAcc_Key.json")

api = Api(  version = "1.0",
            title = "Simple Flask Api",
            description = "This is a simple flask api that implements CRUD \
                            operations with a firebase database")


