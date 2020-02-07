import os
import geoip2.database


def getLoc(ip):
    # 传入下载的数据的地址
    reader = geoip2.database.Reader("./GeoLite2-City_20191126/GeoLite2-City.mmdb")
    data = reader.city(ip)
    print("ip地址：", ip)
    # names['zh-CN']即可转换为中文
    print("国家: ", data.country.names['zh-CN'])
    print("省份: ", data.subdivisions.most_specific.names['zh-CN'])
    print("城市: ", data.city.names['zh-CN'])
    print("纬度: ", data.location.latitude)
    print("经度: ", data.location.longitude)

getLoc("192.168.1.6")