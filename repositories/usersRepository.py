from ast import List
import json
from multiprocessing.dummy import Array
import string
import sys

from sqlalchemy import JSON
sys.path.append('.')

from datetime import date, datetime
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin

from models.user import User


class UserRepository:
    def __init__(self, keyFile):

        # Use a service account
        self.__cred = credentials.Certificate(keyFile)
        firebase_admin.initialize_app(self.__cred)
        self.__users_ref = firestore.client().collection("users")


    def getAllUsers(self) -> List(User):
        docs = self.__users_ref.stream()
        userList = []

        for doc in docs:
            userList.append(doc.to_dict())

        return userList


    def getUser(self, cpf):
        doc = self.__users_ref.where("CPF", "==", cpf).get()
        if len(doc) > 0:
            user = doc[0].to_dict()
            return user
        
        return None


    def addUser(self, user: User):
        doc = self.__users_ref.where("CPF", "==", user.CPF).get()
        if user != None and len(doc) < 1:
            try:
                self.__users_ref.document().set(user.toDict())
                return user.toDict()
            except:
                return "Erro adding the user"


    def updateUser(self, user: User):
        doc = self.__users_ref.where("CPF", "==", user.CPF).get()
        if user != None and len(doc) > 0:
            self.__users_ref.document(doc[0].id).set(user.toDict())
            return user.toDict()


    def deleteUser(self, user: User):
        doc = self.__users_ref.where("CPF", "==", user.CPF).get()
        if len(doc) > 0:
            self.__users_ref.document(doc[0].id).delete()
            return "User deleted successfully"
