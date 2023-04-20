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
    digital_approch_title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    cloud_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    cloud_intro = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    cloud_desc = RichTextField(blank=True)
    cloud_right_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )
    cloud_left_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )
    cloud_second_right_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )
    app_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    app_intro = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    app_desc = RichTextField(blank=True)
    digital_revolution_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    digital_transition_title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("desc_of_digital_section"),
        FieldPanel("digital_approch_title"),

        FieldPanel("cloud_title"),
        FieldPanel("cloud_intro"),
        FieldPanel("cloud_desc"),
        FieldPanel("cloud_right_image"),
        FieldPanel("cloud_left_image"),
        FieldPanel("cloud_second_right_image"),

        FieldPanel("app_title"),
        FieldPanel("app_intro"),
        FieldPanel("app_desc"),

        FieldPanel("digital_revolution_title"),
        FieldPanel("digital_transition_title"),

    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Digitalisation Page"


class MissionPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """
    innovation_approch_title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    innovation_approch_small_text = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    innovation_approch_intro = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    innovation_approch_desc = RichTextField(blank=True)
    innovation_approch_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )

    global_approch_title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    global_approch_small_text = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    global_approch_intro = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    global_approch_desc = RichTextField(blank=True)
    global_approch_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )

    transition_approch_title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    transition_approch_small_text = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    transition_approch_intro = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    transition_approch_desc = RichTextField(blank=True)
    transition_approch_image = models.ForeignKey(
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
        FieldPanel("digital_approch_title"),

        FieldPanel("innovation_approch_title"),
        FieldPanel("innovation_approch_small_text"),
        FieldPanel("innovation_approch_intro"),
        FieldPanel("innovation_approch_desc"),
        FieldPanel("innovation_approch_image"),

        FieldPanel("global_approch_title"),
        FieldPanel("global_approch_small_text"),
        FieldPanel("global_approch_intro"),
        FieldPanel("global_approch_desc"),
        FieldPanel("global_approch_image"),

        FieldPanel("transition_approch_title"),
        FieldPanel("transition_approch_small_text"),
        FieldPanel("transition_approch_intro"),
        FieldPanel("transition_approch_desc"),
        FieldPanel("transition_approch_image"),

        FieldPanel("digital_transition_title"),
    ]

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
