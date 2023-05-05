from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import (
    BaseSiteSetting,
    register_setting,
)


@register_setting
class HeaderSettings(BaseSiteSetting):
    """The Header setting model"""
    logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("logo"),
    ]
