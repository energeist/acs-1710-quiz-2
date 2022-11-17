from flask import Flask, request, render_template
from PIL import Image, ImageFilter
from pprint import PrettyPrinter
from dotenv import load_dotenv
import json
import os
import random
import requests

load_dotenv()

app = Flask(__name__)

SWAPI_BASE_URL = 'https://swapi.py4e.com/api/'
SWAPI_PEOPLE_URL = 'https://swapi.py4e.com/api/people/'

@app.route('/swapi', methods=['GET', 'POST'])
def swapi_search():
    if request.method == 'POST':
        search = request.form.get("search_query")
        limit = request.form.get("quantity")
        response = requests.get(
            TENOR_URL,
            {
                # TODO: Add in key-value pairs for:
                'q': search,
                'key': API_KEY,
                'limit': limit
            })

        gifs = json.loads(response.content).get('results')

        context = {
            'gifs': gifs
        }

        # Uncomment me to see the result JSON!
        # Look closely at the response! It's a list
        # list of data. The media property contains a 
        # list of media objects. Get the gif and use it's 
        # url in your template to display the gif. 
        pp.pprint(gifs)
    #     return render_template('gif_search.html', **context)
    # else:
    #     return render_template('gif_search.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)