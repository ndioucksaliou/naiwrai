from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField


@register_snippet
class Carousel(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = RichTextField(
        blank=False,
        null=True,
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("description"),
            ],
        ),
    ]

    def __str__(self) -> str:
        return self.name


class CarouselPageCarouselPlacement(Orderable, models.Model):
    """ Carousel Placement """
    page = ParentalKey(
        'carousel_items.CarouselPage',
        on_delete=models.CASCADE,
        related_name='carousel_placements'
    )
    carousel = models.ForeignKey(
        'carousel_items.Carousel',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('carousel'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.carousel.name

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "carousel placement"
        verbose_name_plural = "carousel placements"


class CarouselPage(Page):  # pylint: disable=too-many-ancestors
    """Carousel page model """
    content_panels = Page.content_panels + [
        InlinePanel('carousel_placements', label="Carousel Item"),
    ]
