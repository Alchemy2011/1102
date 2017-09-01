# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


tornado.options.define('port', default=8000, type=int,
                       help='run server on the given port.')
tornado.options.define('lqr',default=[], type=str, multiple=True,
                       help='lqr subjects.')


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self, *args, **kwargs):
        """对应http的get请求方式"""
        self.write('index 8 ok')
    # def post(self):
    #     """对应http的post请求方式"""
    #     self.write("Hello tornado")


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    tornado.options.parse_config_file("./config")
    print tornado.options.options.lqr
    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
         ],
        debug=True
    )
    # app.listen(8000)  # 简写方式

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    # 学习时，推荐使用方式，
    # 对理解tornado web应用工作流程的完整性有帮助，
    # 便于大家记忆tornado开发的模块组成和程序结构；熟练后可以简写。
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(8000)

    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.bind(8000)
    # http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
