from app import app
from flask import request,jsonify
from models.user_controller import user
from models.recommendation_controller import recommendation
@app.route('/v1/user/get/<username>')
def get_user(username):
	user_object = user()
	if len(username):
		response = user_object.get(username)
		return jsonify(response)
	else:
		raise Exception("No data sent for get user",400)

@app.route('/v1/user/create',methods=['POST'])
def create_user():
	form = request.form
	if not form or len(form) == 0:
		raise Exception("No data sent for create user",400)
	user_object = user()
	response = user_object.create(form)
	return str(response)
	

@app.route('/v1/user/update_state',methods=['POST'])
def update_user_state():
	form = request.form
	if not form or len(form) == 0:
		raise Exception("No data sent for create user",400)
	user_object = user()
	response = user_object.update_state(form)
	return str(response)

@app.route('/v1/user/fetch_rec/<username>',methods=['POST'])
def fetch_recommendation(username):
	form = request.form
	features = ['mood','location','weather','event']
	state = []
	for f in features:
		state.append(form[f])
	user_object = user()
	if len(state) == 0:
		state = user_object.fetch_previous_state(username)
	rec_controller = recommendation()
	response = rec_controller.get_rec(state)
	return str(response)

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
