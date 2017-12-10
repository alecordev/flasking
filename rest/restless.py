import flask
import flask_sqlalchemy
import flask_restless
# import flask.ext.sqlalchemy
# import flask.ext.restless

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = flask_sqlalchemy.SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    birth_date = db.Column(db.Date)
    computers = db.relationship(
        'Computer', uselist=False, back_populates="owner")


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    vendor = db.Column(db.Unicode)
    owner = db.relationship('Person', uselist=False,
                            back_populates="computers")
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    purchase_time = db.Column(db.DateTime)


db.create_all()


manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

print(manager.create_api(Person, methods=['GET', 'POST', 'DELETE']))

manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Computer)

person_blueprint = manager.create_api_blueprint(
    Person, methods=['GET', 'POST'])
computer_blueprint = manager.create_api_blueprint(
    Computer, methods=['GET', 'POST'])

app.register_blueprint(person_blueprint)
app.register_blueprint(computer_blueprint)

app.run(host='0.0.0.0', port=5454, threaded=True)
