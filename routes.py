from app import app
from flask import render_template, request, Response
import json
from src.controllers.TwitterApiController import TwitterApiController

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet')
def get_result():
	controller = TwitterApiController()
	result = controller.fetchTweet(request.args)
	js = json.dumps(result)
	resp = Response(js, status=200, mimetype='application/json')
	return resp
