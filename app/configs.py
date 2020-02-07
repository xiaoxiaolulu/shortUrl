"""
配置文件
    1.静态文件目录
    2.模板文件目录
    3.调试模式
    4.开启xsrf保护
    5.设置cookie秘钥
"""
import os
root = os.path.dirname(__file__)


configs = dict(
    static_path=os.path.join(root, 'static'),
    template_path=os.path.join(root, 'templates'),
    debug=True,
    xsrf_cookie=True,
    cookie_secret='e0777c52a1df4bf98591a6e843d605f5'
)

mysql_configs = dict(
    db_host="127.0.0.1",
    db_name='shorturl',
    db_port=3306,
    db_user='root',
    db_pwd='123456'
)
