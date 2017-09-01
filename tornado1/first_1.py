# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):  # 处理get类型请求
        self.write('index page5 ok')


class TornadoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):  # 处理get类型请求
        self.write('tornado page ok')

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/', IndexHandler),  # 路由映射表
            (r'/tornado', TornadoHandler)
        ]
        ,
        debug=True
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
