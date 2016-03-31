from app import app
from flask import request,jsonify
from models.user_controller import user
from models.recommendation_controller import recommendation
from models.songs_model import songs
from models.weather_controller import weather 
from models.user_state_history_model import user_state_history
@app.route('/v1/user/get/<username>')
def get_user(username):
	user_object = user()
	if username:
		response = user_object.get({"username":username})
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
	latitude = form['lat']
	longitude = form['lon']
	for f in features:
		if f == 'location' or f == 'event':
			state.append('-')
		elif f == 'weather':
			w = weather()
			state.append(w.get_weather(latitude,longitude))
		elif f == "mood":
			m = user_state_history()
			state.append(m.get_latest(username,"mood_feature"))
	print state
	user_object = user()
	if len(state) == 0:
		state = user_object.fetch_previous_state(username)
	rec_controller = recommendation()
	songs_controller = songs()
	rec_ids = rec_controller.get_rec(state)
	song_uris = songs_controller.get(rec_ids)
	song_uris = [str(s) for s in song_uris]
	song_uris.append("spotify:track:0BF6mdNROWgYo3O3mNGrBc")
	song_uris.append("spotify:track:4O0Yww5OIWyfBvWn6xN3CM")
	song_uris.append("spotify:track:3LlAyCYU26dvFZBDUIMb7a")
	song_uris.append("spotify:track:0YuH7QCFXK0elodziM1cOU")
	return jsonify(uris=song_uris)

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
