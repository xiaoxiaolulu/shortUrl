import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from app.configs import configs, mysql_configs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.urls import urls


define('port', type=int, default=8000, help='运行端口')


class CustomApplication(tornado.web.Application):

    def __init__(self):
        setting = configs
        handlers = urls
        self.db = self.db_session
        print(urls)
        super(CustomApplication, self).__init__(handlers=handlers, **setting)

    @property
    def db_session(self):
        engine = create_engine(
            'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(**mysql_configs),
        )
        session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False
        )
        return session()



def create_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(
        CustomApplication(),
        xheaders=True
    )
    print(options.port)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
