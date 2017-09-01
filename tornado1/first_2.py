# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config
from tornado.web import url

# 自定义启动参数选项，用变量可以实现选项的想过？为什么要看似多此一举？
# 为了实现从配置文件输出参数做准备
tornado.options.define('port', default=8000, type=int,
                       help='run server on given port.')
# port= 8000
# 自定义可多个启动参数
tornado.options.define('lqr', [], type=str, multiple=True,
                       help='lqr information')


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index ok')


class TornadoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('tornado ok')


class GetHandler(tornado.web.RequestHandler):
    # 根据需求获取url中的参数，你用户爱传什么都行，我只获取我需要的a，b
    def get(self, *args, **kwargs):  # get接口
        # a = self.get_query_argument('a', default=None)  # 获取get请求类型 查询参数a的值
        # b = self.get_query_argument('b', default=None)  # 获取get请求类型 查询参数b的值
        # print a, b
        # a_list = self.get_query_arguments('a')  # 获取同一个名称的多个值
        # print type(a_list)
        # print a_list
        # self.write('get ok')
        self.render('reg.html')

    def post(self, *args, **kwargs):  # post接口
        # 从html的form表单中获取的name属性对应的输入框里的值
        username = self.get_body_argument(name='username', default=None)  # name是什么？在哪？
        password = self.get_body_argument(name='password', default=None)
        print username, password  # 调试信息
        if username and password:
            if username == 'liqirong' and password == '111111':
                # 做一个响应
                self.write('你好，李启荣，登陆成功')
            else:
                self.write('登陆失败，再试一试')
        else:
            self.write('用户名和密码，不能为空')


if __name__ == '__main__':
    # 解析命令行，选项从命令行解析
    # tornado.options.options.parse_command_line()  # 从命令行接收启动参数
    # print tornado.options.options.lqr

    # 如何将启动参数放到一个.txt文本文档配置文件启动
    # 解析命令文件
    # tornado.options.options.parse_config_file('./config')
    # print tornado.options.options.lqr

    # 从.py配置文件导入配置参数
    tornado.options.options.parse_config_file('config')
    print config.lqr

    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
            url(r'/tornado', TornadoHandler, name='tornado'),
            url(r'/get', GetHandler, name='get')
        ]
        # 给路由其别名，name在模板中可以用，在get接口中也可以用
        ,
        # debug=True,  # 放到settings里面了
        **config.settings

    )
    # 从config.py的配置文件导入启动参数的话，就需要加到服务里面
    http_server = tornado.httpserver.HTTPServer(app, config.settings)

    # http_server = tornado.httpserver.HTTPServer(app)

    # 从.py配置文件导入启动参数
    # http_server.bind(8000)
    http_server.bind(config.port)

    # 从普通.txt文本文档导入启动参数，
    # 最多只支持到列表
    # http_server.bind(tornado.options.options.port)  # 调用选项

    # http_server.bind(port)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
