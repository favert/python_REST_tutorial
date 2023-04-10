# app.py
from flask import Flask, request, jsonify
from markupsafe import escape


app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

def _delete_country(id):
    for i in range(len(countries)):
        if (countries[i]["id"] == id):
            countries.pop(i)
            return 1
    return 0

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

# note: does not need jasonify for element, only for lists (flask limitation)
@app.get("/country")
def get_country():
    return countries[2]

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    if _delete_country(id):
        return "", 204
    return {"error":"Element not found"}, 422