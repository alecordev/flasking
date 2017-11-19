import os
from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return Response('Index')


if __name__ == "__main__":
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    context = (os.path.join(current_file_dir, 'localhost.crt'),
               os.path.join(current_file_dir, 'localhost.key'))
    app.run(host='0.0.0.0', port=8080,
            ssl_context=context, threaded=True, debug=True)
