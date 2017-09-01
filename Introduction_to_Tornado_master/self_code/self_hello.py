import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import options, define

define('port', default=8000, help='run on the given port', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ',good morning')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler)
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
