from abc import ABC
from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, URL
from app.models.short_link import ShortUrl
from app.views.views_common import CommonHandler
from werkzeug.datastructures import MultiDict


class ShortUrlForm(Form):

    url = StringField(
        "链接",
        validators=[
            DataRequired('链接不能为空'),
            URL(message="链接格式不正确！")
        ]
    )


class IndexHandler(CommonHandler, ABC):

    def get(self, *args, **kwargs):
        data = dict(
            title="生成短链接"
        )
        self.render('index.html', data=data)

    def post(self, *args, **kwargs):
        res = dict(code=0)
        form = ShortUrlForm(MultiDict(self.params))

        if form.validate():

            try:
                short_url = self.session.query(ShortUrl).filter_by(
                    url=form.data['url']
                ).first()

                if not short_url:

                    import uuid
                    uuid_data = uuid.uuid4().hex
                    short_link = ShortUrl(
                        url=form.data['url'],
                        code=self.get_hash_key(form.data['url'])[0],
                        uuid=uuid_data,
                        createDAt=self.dt,
                        updatedAt=self.dt
                    )
                    self.session.add(short_link)
                else:
                    uuid_data = short_url.uuid
                res['code'] = 1
                res['uuid'] = uuid_data
            except Exception as msg:
                self.session.rollback()
                print(msg)
            else:
                self.session.commit()
            finally:
                self.session.close()
        else:
            res = form.errors
            res['code'] = 0
        self.write(res)
