from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from flask_app import app


class MainHandler(RequestHandler):
    def get(self):
        self.write('Tornado')


application = Application([
    (r"/tornado", MainHandler),
    (r".*", FallbackHandler, dict(fallback=WSGIContainer(app))),
])


if __name__ == "__main__":
    application.listen(8000)
    IOLoop.instance().start()
