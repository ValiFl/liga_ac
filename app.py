from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    who = request.args.get('who', 'World')
    where = request.args.get('where', '')
    return f"Hello {who} {where}!"


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug =True)


