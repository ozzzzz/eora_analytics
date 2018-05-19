from flask import Flask, jsonify, request
from flask_cors import CORS
from server.teams_data import teams_initial
from server.hacks_data import hacks_initial
from server.users_data import users_initial

app = Flask(__name__)
CORS(app)
#
# d = [
#     {"y": 3, "label": "Sweden"},
#     {"y": 7, "label": "Taiwan"},
#     {"y": 5, "label": "Russia"},
#     {"y": 9, "label": "Spain"},
#     {"y": 7, "label": "Brazil"},
#     {"y": 7, "label": "India"},
#     {"y": 9, "label": "Italy"},
#     {"y": 8, "label": "Australia"},
#     {"y": 11, "label": "Canada"},
#     {"y": 15, "label": "South Korea"},
#     {"y": 12, "label": "Netherlands"},
#     {"y": 15, "label": "Switzerland"},
#     {"y": 25, "label": "Britain"},
#     {"y": 28, "label": "Germany"},
#     {"y": 29, "label": "France"},
#     {"y": 52, "label": "Japan"},
#     {"y": 103, "label": "China"},
#     {"y": 105, "label": "US"}
# ]

teams = teams_initial.copy()
hacks = hacks_initial.copy()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/stats/teams')
def stats_teams():
    with_y = []
    for item in teams:
        with_y.append({'label': item['name'], 'y': item['score']})
    return jsonify(with_y)


@app.route('/stats/hacks')
def stats_hacks():
    with_y = []
    for item in hacks:
        with_y.append({'label': item['name'], 'y': item['score']})
    return jsonify(with_y)


pair = (0, 1)
users = users_initial.copy()


@app.route('/vote')
def vote():
    (fst_index, snd_index) = pair
    first = users[fst_index]
    second = users[snd_index]
    return jsonify([first, second])


@app.route('/vote_set', methods=['POST'])
def vote_set():
    data = request.get_json(force=True)
    print("DATA", data)
    users_initial[data]['score'] = users_initial[data]['score'] + 1
    update_pair()
    return jsonify(data)
#     elems = filter(lambda x: x['label'] == data['label'], d)
#     for e in elems:
#         d[e['label']] = e
#     # show the post with the given id, the id is an integer
#     # print(vote_id)
#     # d[]
#     # print(d)
#     # return "Post {}".format(vote_id)
#     return jsonify(d)


def update_pair():
    global pair
    fst = (pair[0] + 1) % 5
    snd = (pair[1] + 1) % 5
    pair = (fst, snd)
