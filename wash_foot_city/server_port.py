# -*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import config


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index is very ok')


class BootstrapHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('Bootstrap.html')


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
            (r'/bootstrap', BootstrapHandler)
        ],
        **config.settings
    )
    app.listen(config.port, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
