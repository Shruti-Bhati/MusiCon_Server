from app import app
from flask import request,jsonify
from user.controller import user

@app.route('/v1/user/save_state',methods=['POST'])
def user_question():
	form = request.form
	if not form or len(form) == 0:
		raise Exception("Error","No data sent for state update")
	u_controller.update_state(form)
	return 200

@app.route('/v1/user/create',methods=['POST'])
def create_user():
	form = request.form
	if not form or len(form) == 0:
		raise Exception("Error","No data sent for create user")
	user_object = user()
	response = user_object.create(form)
	return response
	
@app.errorhandler(500)
def internal_server_error(error):
	print "Internal server error ",error
	if error:
		msg,code = error.args
		response = jsonify({"Response":msg})
		response.status_code = code
	else:
		response = jsonify({"Response":"Please check back later.Server is experiencing problems"})
		response.status_code = 500
	return response
