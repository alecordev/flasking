from flask import Flask, Blueprint

app = Flask(__name__)
api = Blueprint('api', __name__)
app.register_blueprint(api, url_prefix='/api/v1')


@app.route('/')
def index():
    return 'Index'


@api.route('/')
def api_index():
    return 'API index page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
