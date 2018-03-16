import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
            "username",
            required= True,
            type = str,
            help = "this field can't be left blank"
		)
	parser.add_argument(
			"password",
			required = True,
			type = str,
			help = "this field can't be left blank"
		)
	def post(self):
		req_data = UserRegister.parser.parse_args()
		if UserModel.find_by_username(req_data["username"]):
			return {"message": "the username already exists"}, 400
		user = UserModel(**req_data)
		user.save_to_db()

		return {"message": "User created successfully."} , 201