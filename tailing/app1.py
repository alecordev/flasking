from time import sleep
from flask import Flask, render_template
from math import sqrt

app = Flask(__name__)


@app.route('/')
def index():
    # render the template (below) that will use JavaScript to read the stream
    return render_template('page1.html')


@app.route('/stream_sqrt')
def stream():
    def generate():
        for i in range(500):
            yield '{}\n'.format(sqrt(i))
            sleep(1)

    return app.response_class(generate(), mimetype='text/plain')


app.run()
