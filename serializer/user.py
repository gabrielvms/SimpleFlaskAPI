from api import api
from flask_restx import fields


user = api.model("User", {
                "CPF": fields.String(readonly=True),
                "Name": fields.String(readonly=True),
                "Surname": fields.String(readonly=True),
                "Age": fields.Integer(readonly=True),
                "Employment_Status": fields.Boolean(readonly=True),
                "Educational_Background": fields.String(readonly=True)
        })