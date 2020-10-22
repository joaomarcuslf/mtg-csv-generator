from flask import Flask, render_template

import requests

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK"

@app.route('/report')
def report():
    return "WIP"

@app.route('/')
def home():
    response = requests.get('https://www.codewars.com/api/v1/users/joaomarcuslf')
    content = response.json()

    data = map_resquest_to_data(content)

    return render_template('index.html', data=data)

def map_resquest_to_data(content):
    keys = [
        "username",
        "name",
        "honor",
        "clan",
        "leaderboardPosition",
        "skills",
    ]

    data = {
        'title': 'MTG CSV Generator',
        'sitename': 'http://joaomarcuslf.com'
    }

    for key in keys:
        data[key] = content[key]

    data['completedKatas'] = content['codeChallenges']['totalCompleted']
    data['overallRank'] = content['ranks']['overall']['name']
    data['languages'] = {}

    for language in content['ranks']['languages']:
        data['languages'][language] = content['ranks']['languages'][language]['name']

    return data

if __name__ == '__main__':
    app.run(debug=True)