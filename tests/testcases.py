from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from needle.cases import NeedleTestCase
from needle.driver import NeedlePhantomJS


class PhantomJSDriver(NeedlePhantomJS):
    def __init__(self, *args, **kwargs):
        path = './node_modules/.bin/phantomjs'
        kwargs.setdefault('executable_path', path)
        return super().__init__(*args, **kwargs)


class ScreenshotTestCase(NeedleTestCase, StaticLiveServerTestCase):
    save_baseline = settings.OVERWRITE_SCREENSHOTS

    @classmethod
    def get_web_driver(cls):
        return PhantomJSDriver()
