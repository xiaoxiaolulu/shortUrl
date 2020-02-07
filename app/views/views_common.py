import datetime
import hashlib
from abc import ABC
import tornado.web


class CommonHandler(tornado.web.RequestHandler, ABC):

    @property
    def site_url(self):
        return 'http://localhost:8000/'

    @property
    def dt(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @property
    def session(self):
        return self.application.db

    @property
    def params(self):
        data = self.request.arguments
        data = {
            v[0]: list(
                map(
                    lambda val: str(val, encoding='utf-8'),
                    v[1]
                )
            )
            for v in data.items()
        }
        return data

    def get_md5(self, s):
        s = s.encode('utf8')
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()

    code_map = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', '0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    )

    def get_hash_key(self, long_url):
        hkeys = []
        hex = self.get_md5(long_url)
        for i in range(0, 4):
            n = int(hex[i * 8:(i + 1) * 8], 16)
            v = []
            e = 0
            for j in range(0, 5):
                x = 0x0000003D & n
                e |= ((0x00000002 & n) >> 1) << j
                v.insert(0, self.code_map[x])
                n = n >> 6
            e |= n << 5
            v.insert(0, self.code_map[e & 0x0000003D])
            hkeys.append(''.join(v))
        return hkeys

    def get(self, *args, **kwargs):
        self.write(str(self.get_hash_key('https://www.cnblogs.com/Zzbj/p/10212279.html')))

