from flask import Flask, jsonify

app = Flask(__name__)

lentokentat = {
    "EFHK": {
        "ICAO": "EFHK",
        "Name": "Helsinki Vantaa Airport",
        "Municipality": "Helsinki"
    },
    "EGLL": {
        "ICAO": "EGLL",
        "Name": "Heathrow Airport",
        "Municipality": "London"
    }
}

@app.route('/kenttä/<string:icao>', methods=['GET'])
def hae_kentan_tiedot(icao):
    if icao in lentokentat:
        return jsonify(lentokentat[icao])
    else:
        return jsonify({"error": "Lentokenttää ei löydy"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)

