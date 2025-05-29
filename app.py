from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/persons', methods=['GET'])
def get_persons():
    response = requests.get("https://randomuser.me/api/?results=10&nat=us")

    if response.status_code != 200:
        return jsonify({"error": "No se pudieron obtener los datos"}), 500

    data = response.json()
    persons = []

    for user in data["results"]:
        person = {
            "nombre": f"{user['name']['first']} {user['name']['last']}",
            "genero": user["gender"],
            "ubicacion": f"{user['location']['city']}, {user['location']['country']}",
            "correo_electronico": user["email"],
            "fecha_nacimiento": user["dob"]["date"][:10],
            "fotografia": user["picture"]["large"]
        }
        persons.append(person)

    return jsonify(persons)

if __name__ == '__main__':
    app.run(debug=True)
