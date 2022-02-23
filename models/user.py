import json
import datetime
import time

class User:

    def __init__(self, cpf, name, surname, age, employment_status, educational_background):
        self.__cpf = cpf
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__employment_status = employment_status
        self.__educational_background = educational_background

    def __init__(self, userDict):
        self.__cpf = userDict["CPF"]
        self.__name = userDict["Name"]
        self.__surname = userDict["Surname"]
        self.__age = userDict["Age"]
        self.__employment_status = userDict["Employment_Status"]
        self.__educational_background = userDict["Educational_Background"]
    
    def __getCpf(self):
        return self.__cpf

    def __setCpf(self, cpf):
        self.__cpf = cpf

    def __getName(self):
        return self.__name

    def __setName(self, name):
        self.__name = name

    def __getSurname(self):
        return self.__surname

    def __setSurname(self, surname):
        self.__surname = surname

    def __getAge(self):
        return self.__age
    
    def __setAge(self, age):
        self.__age = age


    def __getEmploymentStatus(self):
        return self.__employment_status

    def __setEmploymentStatus(self, employment_status):
        self.__employment_status = employment_status

    def __getEducationalBackground(self):
        return self.__educational_background

    def __setEducationalBackground(self, educational_background):
        self.__educational_background = educational_background
    
    CPF = property(__getCpf, __setCpf)
    Name = property(__getName, __setName)
    Surname = property(__getSurname, __setSurname)
    Age = property(__getAge, __setAge)
    Employment_Status = property(__getEmploymentStatus, __setEmploymentStatus)
    Educational_Background = property(__getEducationalBackground, __setEducationalBackground)

    def toDict(self):
        return {
            "CPF": self.CPF,
            "Name": self.Name,
            "Surname": self.Surname,
            "Age": self.Age,
            "Employment_Status": self.Employment_Status,
            "Educational_Background": self.Educational_Background
        }
