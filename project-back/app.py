# Imports
from flask import Flask, jsonify, request, url_for, json
from flask_cors import CORS
from flask_socketio import SocketIO
import time

# Custom imports
from database.DP1Database import Database
from domein import cocktail_machine, lcd
from subprocess import check_output


# Start app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret!'
CORS(app)
socketio = SocketIO(app)

conn = Database(app=app, user='mct', password='mct', db='cocktailmaker')
machine = cocktail_machine.cocktailmachine()
lcd = lcd.Lcd()
time.sleep(30)

def display_ip():
    ip = check_output(['hostname', '--all-ip-addresses'])
    ips = ip.split()
    try:
        lcd.send_instruction(0b00000001)
        lcd.write_message("IP-adres:")
        lcd.new_line()
        lcd.write_message(str(ips[0])[2:-1])
    except:
        lcd.send_instruction(0b00000001)
        lcd.write_message("geen IP adres")
        lcd.new_line()
        lcd.write_message("beschikbaar")

display_ip()

# Custom endpoint
endpoint = '/api/v1'

# TESTROUTE
@app.route(endpoint + '/')
def test():
    return jsonify("connected succesfully"),201

@app.route(endpoint + '/dranken')
def get_dranken():
    try:
        return jsonify(conn.get_data('select * from cocktailmaker.dranken')),201
    except:
        return jsonify("er ging iets mis bij het ophalen van de dranken"), 500

@app.route(endpoint + '/dranken/spirits')
def get_spirits():
    try:
        return jsonify(conn.get_data('select * from cocktailmaker.dranken inner join spirits on id_drank = drank_id')),201
    except:
        return jsonify("er ging iets mis bij het ophalen van de spirits"), 500

@app.route(endpoint + '/dranken/softs')
def get_softs():
    try:
        return jsonify(conn.get_data('select * from cocktailmaker.dranken inner join softs on id_drank = drank_id')),201
    except:
        return jsonify("er ging iets mis bij het ophalen van de softs"), 500

@app.route(endpoint + '/cocktails')
def get_cocktails():
    try:
        return jsonify(conn.get_data('select * from cocktailmaker.cocktails')),201
    except:
        return jsonify("er ging iets mis bij het ophalen van de cocktails"),500

@app.route(endpoint + '/logboek')
def get_loggings():
    try:
        return jsonify(conn.get_data('select * from cocktailmaker.cocktaillogboek join cocktails on id_cocktail = cocktail_id order by datum desc;')),201
    except:
        return jsonify("er ging iets mis bij het ophalen van het logboek"),500

@app.route(endpoint + '/dranken/beschikbaar')
def get_dranken_beschikbaar():
    try:
        return jsonify(conn.get_data('select * from cocktailmaker.dranken where pomp_drank is not null')),201
    except:
        return jsonify("er ging iets mis bij het ophalen van de beschikbare dranken"), 500

@app.route(endpoint + '/dranken/soorten')
def get_soorten():
    try:
        return jsonify(conn.get_data('select soort_drank from cocktailmaker.spirits')), 201
    except:
        return jsonify("er ging iets mis bij het ophalen van de soorten"),500

@app.route(endpoint + '/cocktail/<code>')
def make_cocktail(code):
    try:
        m = machine.maak_cocktail(code)
        if m == "cocktail werd succesvol gemaakt":
            d = conn.get_data("select id_cocktail from cocktails where code_cocktail = '{0}';".format(code))
            a = conn.set_data('insert into cocktaillogboek (aantal, cocktail_id) values (1, {0});'.format(d[0]["id_cocktail"]))
            display_ip()
        return jsonify(m), 201
    except:
        return jsonify("er ging iets mis bij het maken van de cocktail"), 500

# Start app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
