from django.contrib import admin
from django import forms
from djangocms_text_ckeditor.fields import HTMLFormField
from designsafe.apps.notifications.models import SiteMessage


class SiteMessageAdminForm(forms.ModelForm):
    """Custom admin form for SiteMessage with WYSIWYG editor."""

    message = HTMLFormField()

    class Meta:
        model = SiteMessage
        fields = '__all__'


class SiteMessageAdmin(admin.ModelAdmin):
    """Admin interface for SiteMessage with WYSIWYG editor."""
    form = SiteMessageAdminForm
    list_display = ('message', 'display')
    list_filter = ('display',)


# Register your models here.
admin.site.register(SiteMessage, SiteMessageAdmin)
