from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from needle.cases import NeedleTestCase
from needle.driver import NeedlePhantomJS


class PhantomJSDriver(NeedlePhantomJS):
    def __init__(self, *args, **kwargs):
        path = './node_modules/.bin/phantomjs'
        kwargs.setdefault('executable_path', path)
        return super().__init__(*args, **kwargs)


class ScreenshotTestCase(NeedleTestCase, StaticLiveServerTestCase):
    engine_class = 'needle.engines.perceptualdiff_engine.Engine'
    save_baseline = settings.OVERWRITE_SCREENSHOTS

    @classmethod
    def get_web_driver(cls):
        return PhantomJSDriver()

    def login(self, user):
        """
        I loathe that we have to log in manually. With a form. Like animals.

        FIXME: Find a way to make this work without filling in a form. Just set
               a "session" cookie, or something? I tried. I was defeated.
        """
        self.driver.get(self.live_server_url + '/admin/')
        username = self.driver.find_element_by_id('id_username')
        username.send_keys(user.username)
        password = self.driver.find_element_by_id('id_password')
        password.send_keys(user.raw_password)
        self.driver.find_element_by_css_selector('form').submit()


def admin_url_name(obj, view_type):
    meta = obj._meta
    return 'admin:{app}_{model}_{view}'.format(
        app=meta.app_label,
        model=meta.model_name,
        view=view_type,
    )


def admin_add_url(obj):
    return reverse(admin_url_name(obj, 'add'))


def admin_change_url(obj):
    return reverse(admin_url_name(obj, 'change'), args=[obj.pk])
