#!/home1/arielma1/python/bin/python

from flup.server.fcgi import WSGIServer
from test import app

if __name__ == '__main__':
    WSGIServer(app).run()
