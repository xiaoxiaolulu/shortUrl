from abc import ABC
from app.views.views_common import CommonHandler
from app.models.short_link import ShortUrl


class ResultHandler(CommonHandler, ABC):

    def get(self, *args, **kwargs):
        data = dict(
            title="短链生成结果"
        )

        uuid = self.get_argument('uuid', None)
        if uuid:
            try:
                su = self.session.query(ShortUrl).filter_by(uuid=uuid).first()
                data['su'] = su
                print(su)
            except Exception as msg:
                self.session.rollback()
                print(msg)
            else:
                self.session.commit()
            finally:
                self.session.close()
        self.render("result.html", data=data)
