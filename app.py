from flask import Flask, request, render_template
import json
import os
import random
import requests

app = Flask(__name__)

SWAPI_BASE_URL = 'https://swapi.py4e.com/api/'
SWAPI_PEOPLE_API = 'https://swapi.py4e.com/api/people/'

@app.route('/swapi_search', methods=['GET', 'POST'])
def swapi_search():
    SWAPI_PEOPLE_API = 'https://swapi.py4e.com/api/people/'
    if request.method == 'POST':

        index = request.form.get("index")

        SWAPI_PEOPLE_API = 'https://swapi.py4e.com/api/people/' + index

        response = requests.get(SWAPI_PEOPLE_API)

        # print(json.loads(response.content))
        context = {
            'detail': json.loads(response.content).get('detail'),
            'name': json.loads(response.content).get('name'),
            'height': json.loads(response.content).get('height'),
            'mass': json.loads(response.content).get('mass'),
            'hair_color': json.loads(response.content).get('hair_color'),
            'eye_color': json.loads(response.content).get('eye_color'),
        }
        print(context)
        return render_template('swapi_search.html', **context)
    else:
        return render_template('swapi_search.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)