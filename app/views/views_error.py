from abc import ABC
import tornado.web


class ErrorHandler(tornado.web.RequestHandler, ABC):

    def get(self, *args, **kwargs):
        self.write("<h1>404, 您访问的页面不存在！</h1>")
