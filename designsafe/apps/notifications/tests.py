from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from djangocms_text_ckeditor.fields import HTMLFormField
from designsafe.apps.notifications.models import SiteMessage
from designsafe.apps.notifications.admin import SiteMessageAdmin, SiteMessageAdminForm


class SiteMessageAdminTests(TestCase):
    """Test cases for SiteMessage admin interface."""

    def test_admin_form_uses_html_field(self):
        """Test that the admin form uses HTMLFormField for message field."""
        form = SiteMessageAdminForm()
        self.assertIsInstance(form.fields['message'], HTMLFormField)

    def test_admin_form_validation(self):
        """Test that the admin form validates correctly with HTML content."""
        form_data = {
            'message': '<b>Test message</b> with <a href="#">HTML</a>',
            'display': True
        }
        form = SiteMessageAdminForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_admin_registration(self):
        """Test that SiteMessage is registered with custom admin."""
        site = AdminSite()
        admin = SiteMessageAdmin(SiteMessage, site)
        self.assertEqual(admin.form, SiteMessageAdminForm)
        self.assertEqual(admin.list_display, ('formatted_message', 'display'))
        self.assertEqual(admin.list_filter, ('display',))

    def test_formatted_message_method(self):
        """Test that formatted_message method renders HTML properly."""
        site_message = SiteMessage(
            message='<b>Test</b> message with <code>$WORK</code>',
            display=True
        )
        site = AdminSite()
        admin = SiteMessageAdmin(SiteMessage, site)
        formatted = admin.formatted_message(site_message)
        self.assertEqual(formatted, '<b>Test</b> message with <code>$WORK</code>')
        self.assertEqual(admin.formatted_message.short_description, 'Message')
