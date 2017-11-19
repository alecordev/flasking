from time import sleep
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('page2.html')


@app.route('/stream')
def stream():
    def generate():
        with open('job.log') as f:
            while True:
                yield f.read()  # f.readline()?
                sleep(1)

    # mimetype='text/event-stream'
    return app.response_class(generate(), mimetype='text/plain')


app.run()
