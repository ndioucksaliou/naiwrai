from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):  # pylint: disable=too-many-ancestors
    """The home page model """
    home_description = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("home_description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Home Page"


class DigitalisationPage(Page):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """
    introduction = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )

    desc_of_digital_section = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("desc_of_digital_section"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Digitalisation Page"


class MissionPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Mission Page"


class ContactPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=True,
        default="contact@newrai.fr",
    )
    object = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    message = RichTextField(blank=False)
    conatct_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("desc_of_digital_section"),
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("object"),
        FieldPanel("message"),
        FieldPanel("conatct_image"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Contact Page"
