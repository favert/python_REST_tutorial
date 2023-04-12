# app.py
from flask import Flask, Blueprint, request, jsonify
from markupsafe import escape

from flaskr.db import get_db

bp = Blueprint('countriesAPI', __name__)


def init_countries():
    countries = [
        {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
        {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
        {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
    ]
    print ('Countries initialized.')

def find_countries(id):
    countries = [
        {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
        {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
        {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
    ]
    return countries

def _find_next_id():
    return max(country["id"] for country in countries) + 1

def _delete_country(id):
    for i in range(len(countries)):
        if (countries[i]["id"] == id):
            countries.pop(i)
            return 1
    return 0

@bp.route('/countries', methods=('GET','POST'))
#@app.get("/countries")
def get_countries():
    return jsonify(find_countries(0))

@bp.route('/countries', methods=('GET','POST'))
#@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

# note: does not need jasonify for element, only for lists (flask limitation)
@bp.route('/country', methods=('GET','POST'))
#@app.get("/country")
def get_country():
    return countries[2]

@bp.route('/delete/<int:id>', methods=('GET','POST'))
#@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    if _delete_country(id):
        return "", 204
    return {"error":"Element not found"}, 422