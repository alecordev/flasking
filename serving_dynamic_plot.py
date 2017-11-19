import base64
from io import BytesIO
import matplotlib.pyplot as plt
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/plot1')
def plot1():
    plt.plot(range(10, 20))
    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    d = 'data:image/png;base64,{}'.format(base64.b64encode(img_data.getvalue()).decode('utf-8'))
    return '<img src = "{}"/>'.format(d)
