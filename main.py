
from flask import Flask, request
import parser

app = Flask(__name__)

@app.route('/')
def root():
    return "200: OK!"


@app.route('/getVacancies')
def getVacancies():
    name = request.args.get('name')
    exp = request.args.get('experience')
    sch = request.args.get('schedule')

    return parser.getVacancies(name=name, exp=exp, sch=sch)

if __name__ == '__main__':
    app.run(debug=True, port=8800)
