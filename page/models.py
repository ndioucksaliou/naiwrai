from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField


@register_snippet
class Application(models.Model):
    """The application model"""
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    description = RichTextField(
        blank=False,
        null=True,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("description"),
                FieldPanel("image"),
            ],
        ),
    ]

    def __str__(self) -> str:
        return self.name


class ApplicationPageApplicationPlacement(Orderable, models.Model):
    """Application Page Placement"""
    page = ParentalKey(
        'page.ApplicationPage',
        on_delete=models.CASCADE,
        related_name='application_placements',
    )
    application = models.ForeignKey(
        'page.Application',
        on_delete=models.CASCADE,
        related_name='+'
    )

    class Meta(Orderable.Meta):
        verbose_name = "application placement"
        verbose_name_plural = "application placements"

    panels = [
        FieldPanel('application'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.application.name


class ApplicationPage(Page):
    """The application model"""
    logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    description = RichTextField(
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("description"),
        InlinePanel('application_placements', label="Applications"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Application Page"
