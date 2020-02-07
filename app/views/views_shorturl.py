from abc import ABC
from app.views.views_common import CommonHandler
from app.models.short_link import ShortUrl, PageView


class ShortLinkHandler(CommonHandler, ABC):

    def get(self, code):
        su = None
        try:
            su = self.session.query(ShortUrl).filter_by(code=code).first()
            print(su.url)
        except Exception as msg:
            self.session.rollback()
            print(msg)
        else:
            self.session.commit()
        finally:
            self.session.close()
        self.redirect(su.url)

    def save_pv(self, shortlink_id):
        try:
            pv = PageView(
                ip=self.request.remote_ip,
                url=self.request.url,
                shorturl_id=shortlink_id,
                method=self.request.method,
                address='',
                createdAt=self.dt,
                updatedAt=self.dt
            )
        except Exception as msg:
            self.session.rollback()
            print(msg)
        else:
            self.session.commit()
        finally:
            self.session.close()
