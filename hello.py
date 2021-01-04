from flask import Flask
import requests # https://requests.readthedocs.io/en/master/
import json # https://docs.python.org/3/library/json.html

# https://flask.palletsprojects.com/en/1.1.x/api/

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/random')
def random_cat_pic():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    body = r.json()
    url = body[0]["url"]
    return {"url": url}

@app.route('/id')
def cat_id():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    body = r.json()
    id = body[0]["id"]
    return {"message": id}

@app.route('/breeds')
def cat_breeds():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    body = r.json()
    breeds = body[0]["breeds"]
    return {"types": breeds}

@app.route('/title/<int:number>')
def ghibli_spirited(number):
    r = requests.get('https://ghibliapi.herokuapp.com/films/')
    body = r.json()
    title = body[number]["title"]
    description = body[number]["description"]
    return {"Title": title, "Description": description} 
    
