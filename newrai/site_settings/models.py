from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
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
    
    carousel_item = StreamField(
        [
            (
                "description", blocks.RichTextBlock()
            ),
        ],
        min_num=2,
        max_num=4,
        use_json_field=True,
        blank=True,
        null=True,
    )

    page_item = StreamField(
        [
            (
                "slide",
                blocks.StructBlock(
                    [
                        ("page", blocks.PageChooserBlock(required=False)),
                    ]
                ),
            ),
        ],
        min_num=1,
        max_num=4,
        use_json_field=True,
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("carousel_item"),
        FieldPanel("page_item"),

    ]