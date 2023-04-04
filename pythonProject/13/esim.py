import _mysql_connector
import json

app = Flask(__name__)

connection = _mysql_connector.connect(
    host=
    port=
    database=
    user=
    password=
    autocommit=True

)
@app.route('/airport(<icao>')
def search_airport(icao)
    try:
        sql = f"SELECT indent, name, muncipality FROM aiport WHERE ident = '{icao}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        response = {"ICAO": result [0], "Name": result[1],"Muncipality": result[2]}
        return jsonify(response)

    except ValueError:
        response = {"message" : "invalid request"}
        response_json = json.dumps(response)
        return Response(response=response_json, status=400)