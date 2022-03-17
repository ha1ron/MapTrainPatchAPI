from flask import Flask, jsonify, request
import process as data

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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



@app.route('/')
def index():
    return "Hello, World!"


@app.route('/tutorials', methods=['GET'])
def get_list():
    query2 = request.args
    print(query2)
    query = request.args.get('MONTH')
    query1 = request.args.get('poezd')
    print(query)
    print(query1)
    return jsonify(tutorials)


# http://172.22.202.84:5000//investigationSet?MONTH=202112&poezd=57386388007008
@app.route('/InvestigationSet', methods=['GET'])
def get_investigationSet():
    month = request.args.get('MONTH')
    poezd = request.args.get('poezd')
    set = data.investigationSet(month, poezd)
    return jsonify(set)


@app.route('/InvestigationSFSet', methods=['GET'])
def get_InvestigationSFSet():
    month = request.args.get('MONTH')
    poezd = request.args.get('poezd')
    set = data.investigationSFSet(month, poezd)
    return jsonify(set)


@app.route('/StNumberingSet', methods=['GET'])
def get_stNumberingSet():
    month = request.args.get('MONTH')
    poezd = request.args.get('poezd')
    set = data.stNumberingSet(month, poezd)
    return jsonify(set)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
