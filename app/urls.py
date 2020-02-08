# from app.views.views_error import ErrorHandler as error
from app.views.views_common import CommonHandler
from app.views.view_index import IndexHandler
from app.views.views_result import ResultHandler
from app.views.views_shorturl import ShortLinkHandler
from app.views.view_pageview import PageViewHandler

urls = [
    # (r'/.*', error),
    (r'/', IndexHandler),
    (r'/result', ResultHandler),
    (r'/([a-zA-Z0-9]{6})', ShortLinkHandler),
    (r'/pageview', PageViewHandler)
]
