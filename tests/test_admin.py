from .factories import AdminUserFactory, PostFactory
from .models import Post
from .testcases import admin_add_url, admin_change_url, ScreenshotTestCase


class TestAdminIntegration(ScreenshotTestCase):
    """Tests for admin integration of the SirTrevorField."""
    def test_empty(self):
        """Sirtrevor is rendered empty when there's no content."""
        self.login(AdminUserFactory.create())
        self.driver.get(self.live_server_url + admin_add_url(Post))
        self.assertScreenshot('body', 'admin-field-empty')

    def test_content(self):
        """Sirtrevor content is rendered."""
        self.login(AdminUserFactory.create())
        post = PostFactory.create(content={
            'data': [{
                'type': 'video',
                'data': {'remote_id': 'dQw4w9WgXcQ', 'source': 'youtube'},
            }],
        })
        self.driver.get(self.live_server_url + admin_change_url(post))
        self.assertScreenshot('body', 'admin-field-video')
