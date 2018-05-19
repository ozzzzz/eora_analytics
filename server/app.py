from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

d = [
			{ "y": 3, "label": "Sweden" },
			{ "y": 7, "label": "Taiwan" },
			{ "y": 5, "label": "Russia" },
			{ "y": 9, "label": "Spain" },
			{ "y": 7, "label": "Brazil" },
			{ "y": 7, "label": "India" },
			{ "y": 9, "label": "Italy" },
			{ "y": 8, "label": "Australia" },
			{ "y": 11, "label": "Canada" },
			{ "y": 15, "label": "South Korea" },
			{ "y": 12, "label": "Netherlands" },
			{ "y": 15, "label": "Switzerland" },
			{ "y": 25, "label": "Britain" },
			{ "y": 28, "label": "Germany" },
			{ "y": 29, "label": "France" },
			{ "y": 52, "label": "Japan" },
			{ "y": 103, "label": "China" },
			{ "y": 105, "label": "US" }
		]


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/stats')
def stats():
    return jsonify(d)


@app.route('/vote', methods=['POST'])
def vote():
	data = request.get_json(force=True)
	print(data)
	elems = filter(lambda x: x['label'] == data['label'], d)
	for e in elems:
		d[e['label']] = e
    # show the post with the given id, the id is an integer
    # print(vote_id)
    # d[]
    # print(d)
    # return "Post {}".format(vote_id)
	return jsonify(d)