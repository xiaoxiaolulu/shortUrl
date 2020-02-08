from abc import ABC
from sqlalchemy import and_
from app.views.views_common import CommonHandler
from app.models.short_link import ShortUrl, PageView


class PageViewHandler(CommonHandler, ABC):

    def get(self, *args, **kwargs):
        data = dict(
            title="短链生成结果"
        )
        uuid_data = self.get_argument('uuid', None)
        if uuid_data:
            try:
                su = self.session.query(ShortUrl).filter_by(uuid=uuid_data).first()
                data.update({'su': su})

                all = self.session.query(PageView).filter_by(
                    shorturl_id=su.id
                ).count()

                data.update({'all': all})
                data.update({'day': all})
                try:

                    day = self.session.query(PageView).filter(
                        and_(
                            PageView.shorturl_id == su.id,
                            PageView.createdAt >= (self.d() + " 00:00:00"),
                            PageView.createdAt <= (self.d(1) + " 00:00:00")
                        )
                    ).count()

                    print(day)
                except Exception as msg:
                    print(msg)

            except Exception as msg:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()

        self.render('pageview.html', data=data)

    def post(self, *agrs, **kwargs):
        res = dict(code=0)
        page = self.get_argument("page", 1)
        uuid = self.get_argument("uuid", None)
        page = int(page)

        try:
            num = 5
            pv = self.session.query(PageView, ShortUrl).filter(
                and_(
                    PageView.shorturl_id ==ShortUrl.id,
                    ShortUrl.uuid == uuid
                )
            ).offset((page -1) * num).limit(num)

            res['data'] = [
                dict(
                    id=v.PageView.id,
                    url=v.PageView.url,
                    address=v.PageView.address,
                    ip=v.PageView.ip,
                    method=v.PageView.method,
                    createdAt=v.PageView.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
                    updateAt=v.PageView.updatedAt.strftime('%Y-%m-%d %H:%M:%S')
                )
                for v in pv
            ]

            if res['data']:
                res['code'] = 1
            else:
                res['code'] = 0
        except Exception as e:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
        self.write(res)


