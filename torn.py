from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app

http_server = HTTPServer(WSGIContainer(app))
#in theory, put the URL here and stuff works. yeeeah.
http_server.listen(9999)
IOLoop.instance().start()
