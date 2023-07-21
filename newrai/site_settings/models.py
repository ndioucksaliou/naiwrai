from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
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
            ('list_items', blocks.StructBlock(
                [
                    ('title', blocks.CharBlock()),
                    ('description', blocks.RichTextBlock()),
                    ('image', ImageChooserBlock(required=False)),
                    ("page", blocks.PageChooserBlock(required=False)),
                ],
            ),
            ),
        ],
        max_num=6,
        use_json_field=True,
        blank=True,
        null=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("carousel_item"),
    ]


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    """The social Media Settings"""
    facebook = models.URLField(
        max_length=100, blank=True, null=True, help_text="FaceBook URL"
    )
    linkedin = models.URLField(
        max_length=100, blank=True, null=True, help_text="LinkedIn URL"
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("linkedin"),
            ],
            heading="Social Media Settings",
        )
    ]
