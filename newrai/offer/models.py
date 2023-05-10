from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey


@register_snippet
class Offer(models.Model):
    """ The Offer model """
    box_class = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        help_text="Donner la class comportant le background color du box"
    )
    icon_class = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        help_text="Donner la class comportant le background color de l'icon "
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    description = RichTextField(
        blank=True,
        null=True,
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("box_class"),
                FieldPanel("icon_class"),
                FieldPanel("title"),
                FieldPanel("description"),
            ]
        )
    ]

    def __str__(self) -> str:
        return str(self.title)


class DigitalOfferPageOfferPlacement(Orderable, models.Model):
    """The OfferPlacement model"""
    page = ParentalKey(
        "offer.DigitalOfferPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="offer_placements"
    )
    offer = models.ForeignKey(
        "offer.Offer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        FieldPanel('offer'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.offer.title

    class Meta(Orderable.Meta):  # pylint: disable=too-few-public-methods
        """ The meta model"""
        verbose_name = "offer placement"
        verbose_name_plural = "offer placements"


class DigitalOfferPage(Page):  # pylint: disable=too-many-ancestors
    """The Digital Offer Model"""
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
        InlinePanel("offer_placements", label="Offer"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Digital Offer Page"
