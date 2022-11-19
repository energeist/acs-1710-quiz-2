# Need to do pip3 install flask[async] to run async functions

from flask import Flask, request, render_template
import json
import os
import random
import requests

app = Flask(__name__)

SWAPI_BASE_URL = 'https://swapi.py4e.com/api/'
SWAPI_PEOPLE_API = 'https://swapi.py4e.com/api/people/'

@app.route('/', methods=['GET', 'POST'])
def swapi_search():
    SWAPI_PEOPLE_API = 'https://swapi.py4e.com/api/people/'
    if request.method == 'POST':
        index = request.form.get("index")
        SWAPI_PEOPLE_API = 'https://swapi.py4e.com/api/people/' + index
        
        try:            
            response = requests.get(SWAPI_PEOPLE_API)
  
        except KeyError:
            context = {
                'detail': 'Not found'
            }

        if json.loads(response.content).get('detail') == 'Not found':
            
            # give 'no data exists' API repsonse to render 404
            context = {
                'detail': 'Not found'
            }            
        else:
            # give 'data exists' API response to render received details 
            # print(json.loads(response.content))
            context = {
                'name': json.loads(response.content).get('name'),
                'height': json.loads(response.content).get('height'),
                'mass': json.loads(response.content).get('mass'),
                'hair_color': json.loads(response.content).get('hair_color'),
                'eye_color': json.loads(response.content).get('eye_color'),
            }
            films_list = json.loads(response.content).get('films')
            print(films_list)
            
            # homeworld search 
            try:
                homeworld_response = requests.get(json.loads(response.content).get('homeworld'))
                homeworld = json.loads(homeworld_response.content).get('name')
                context['homeworld'] = homeworld
            except KeyError:
                context['homeworld'] = ''
            
            # movie search
            movie_titles = []
            try:
                for film in films_list:
                    film_response = requests.get(film)
                    print(json.loads(film_response.content).get('title'))
                    movie_titles.append(json.loads(film_response.content).get('title'))
                context['movies'] = movie_titles
            except KeyError:
                context['movies'] = ''

        return render_template('swapi_search.html', **context)
    else:
        return render_template('swapi_search.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)