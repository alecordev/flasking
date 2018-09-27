""" https://getbootstrap.com/docs/4.1/components/forms/ """

import logging

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request
)

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] - %(message)s')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    selection = ['Option 1', 'Option 2']
    if request.method == 'POST':
        option = request.form.get('selection')
        date = request.form.get('date')
        checkbox = bool(request.form.get('checkboxIdentifier'))
        print([option, date, checkbox])
        return render_template('index.html', selections=selection)
    else:
        return render_template('index.html', selections=selection)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)