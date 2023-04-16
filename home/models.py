from django.db import models

from wagtail.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):  # pylint: disable=too-many-ancestors
    """The home page model """
    home_description = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("home_description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Home Page"
