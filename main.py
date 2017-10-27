from flask import Flask, request, render_template, jsonify
app = Flask(__name__, static_url_path='')
import os 
from detect_intent import _detect_text_intent

@app.route('/')
def index():
	'''
	Home page
	'''

	return render_template('index.html')

@app.route('/run_test_intent')
def detect_test():
	print "HEMANTH is Here"
	#print _detect_text_intent("dialogflow-enterprise-demo", "NewAgent", "b83b2284-7a36-46f7-b220-e33ed3d78722", request.args["input_string"], "en-US").fulfillment.text
	return _detect_text_intent("dialogflow-enterprise-demo", "NewAgent", "b83b2284-7a36-46f7-b220-e33ed3d78722", request.args["input_string"], "en-US").fulfillment.text

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8000))
	app.run(debug=True, host='0.0.0.0', port=port)