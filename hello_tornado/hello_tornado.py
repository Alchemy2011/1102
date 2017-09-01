import tornado.web
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index ok')


if __name__ == "__main__":
    app = tornado.web.Application(
        [r'/', IndexHandler]
    )
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.bind(8000)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
