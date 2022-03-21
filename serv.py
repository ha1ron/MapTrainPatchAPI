from flask import Flask, jsonify, request, redirect, url_for, make_response
import process as data
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'f76v7v67x6v7dx6v876dx7vdx8'

auth = HTTPBasicAuth()

tutorials = [
    {
        'id': 1,
        'title': 'Строка 1',
        'description': 'Описание 1'
    },
    {
        'id': 2,
        'title': 'Строка 2',
        'description': 'Описане 2'
    }
]


@auth.get_password
def get_password(username):
    if username == 'ocrv':
        return 'ocrv'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/tutorials', methods=['GET'])
@auth.login_required
def get_list():
    query2 = request.args
    print(query2)
    query = request.args.get('MONTH')
    query1 = request.args.get('poezd')
    print(query)
    print(query1)
    return jsonify(tutorials)


# http://172.22.202.84:5000/InvestigationSet?MONTH=202112&poezd=57386388007008
@app.route('/InvestigationSet', methods=['GET'])
@auth.login_required
def get_investigationSet():
    month = request.args.get('MONTH')
    poezd = request.args.get('poezd')
    set = data.investigationSet(month, poezd)
    return jsonify(set)


@app.route('/InvestigationSFSet', methods=['GET'])
@auth.login_required
def get_InvestigationSFSet():
    month = request.args.get('MONTH')
    poezd = request.args.get('poezd')
    set = data.investigationSFSet(month, poezd)
    return jsonify(set)


@app.route('/StNumberingSet', methods=['GET'])
@auth.login_required
def get_stNumberingSet():
    month = request.args.get('MONTH')
    poezd = request.args.get('poezd')
    set = data.stNumberingSet(month, poezd)
    return jsonify(set)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
