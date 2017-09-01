# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.options


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index ok')


if __name__ == "__main__":
    tornado.options.options.parse_config_file('./config')
    app = tornado.web.Application(
        [
            (r"/", IndexHandler)
        ]
    )
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
