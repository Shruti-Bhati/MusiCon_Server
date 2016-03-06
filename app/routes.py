from app import app
from flask import request,jsonify

@app.route('/v1/user/save_state',methods=['POST'])
def user_question():
	print vars(request)
