from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from offer.models import DigitalOfferPage


@register_snippet
class WhyChooseNewrai(models.Model):
    """ The home model"""
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    description = RichTextField(
        null=True,
        blank=True,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("icon"),
                FieldPanel("description"),

            ]
        )
    ]

    def __str__(self) -> str:
        return str(self.name)


class WhyChooseNewraiPageChooseNewraiPlacement(Orderable, models.Model):
    """ The home placement """
    page = ParentalKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="whychoosenewrai_items"
    )
    whychoosenewrai = models.ForeignKey(
        "home.WhyChooseNewrai",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('whychoosenewrai'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.whychoosenewrai.name

    class Meta(Orderable.Meta):  # pylint: disable=too-few-public-methods
        """ The meta model"""
        verbose_name = "whychoosenewrai placement"
        verbose_name_plural = "whychoosenewrai placements"


@register_snippet
class Trusts(models.Model):
    """ The home model"""
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("logo"),
            ]
        )
    ]

    def __str__(self) -> str:
        return str(self.name)


class TrustsPageTrustsPlacement(Orderable, models.Model):
    """ The home placement """
    page = ParentalKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="trusts_items"
    )
    trusts = models.ForeignKey(
        "home.Trusts",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('trusts'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.trusts.name

    class Meta(Orderable.Meta):  # pylint: disable=too-few-public-methods
        """ The meta model"""
        verbose_name = "trust placement"
        verbose_name_plural = "trust placements"


class HomePage(Page):  # pylint: disable=too-many-ancestors
    """The home page model """
    # ==================== Hero Section Model========================
    home_description = RichTextField(blank=True)
    home_image_logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    slogan_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter le titre du slogan",
    )
    slogan_description = RichTextField(blank=True)
    slogan_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    # ==================== Offer Section Model ==================

    # ===================== Mission Section Model =========================
    home_title_mission = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter le titre de vision",
    )
    home_image_mission = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    youtube_url = models.URLField(
        null=True,
        blank=True,
        help_text='Your YouTube channel or user account URL',
    )
    first_intro_mission = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter la 1ére introduction de mission",
    )
    second_intro_mission = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter la 2ème introduction de mission",
    )
    first_desc_mission = RichTextField(blank=True)
    second_desc_mission = RichTextField(blank=True)
    # ====================== Vision Section Model =============================
    home_image_vision = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    home_title_vision = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter le titre de vision",
    )

    home_intro_vision = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter l'introduction de vision",
    )

    home_desc_vision = RichTextField(blank=True)

    # =================== Commitment Section Model ============================
    home_image_commitment = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    home_title_commitment = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter le titre d'engagement",
    )
    home_desc_commitment = RichTextField(blank=True)

    trust_intro = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    why_choose_newrai_intro = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        # ======= Hero Section panel
        MultiFieldPanel(
            [
                FieldPanel("home_description", heading="Description"),
                FieldPanel("home_image_logo", heading="Image Logo"),
            ],
            heading="Home",
        ),

        MultiFieldPanel(
            [
                FieldPanel("slogan_title", heading="Title"),
                FieldPanel("slogan_description", heading="Description"),
                FieldPanel("slogan_image", heading="Image slogan"),
            ],
            heading="Slogan",
        ),

        # ======= Mission Section Pannel
        MultiFieldPanel(
            [
                FieldPanel("home_title_mission", heading="Title"),
                FieldPanel("home_image_mission", heading="Image"),
                FieldPanel("youtube_url", heading="Lien de la vidéo"),
                InlinePanel("related_items_for_home", label="mission item")
            ],
            heading="Mission",
        ),

        # ========= Vision Section Panel

        MultiFieldPanel(
            [
                FieldPanel("home_image_vision", heading="Image"),
                FieldPanel("home_title_vision", heading="Title"),
                FieldPanel("home_intro_vision", heading="Introduction"),
                FieldPanel("home_desc_vision", heading="Description"),
            ],
            heading="Vision",
            # classname="collapsed",
        ),

        # ========= Commitment Section Panel
        MultiFieldPanel(
            [
                FieldPanel("home_image_commitment", heading="Image"),
                FieldPanel("home_title_commitment", heading="Title"),
                FieldPanel("home_desc_commitment", heading="Description"),
            ],
            heading="Commitment",
        ),
        MultiFieldPanel(
            [
                FieldPanel("trust_intro", heading="Introduction"),
                InlinePanel("trusts_items", label="Trusts"),
            ],
            heading="Trust",
        ),
        MultiFieldPanel(
            [
                FieldPanel("why_choose_newrai_intro", heading=""),
                InlinePanel("whychoosenewrai_items", label="Why Choose Newrai"),
            ],
            heading="Why choose Newrai",
        )
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        apps = DigitalOfferPage.objects.live().public().order_by("-first_published_at")
        context["apps"] = apps
        return context

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Home Page"


class DetailPage(Page):  # pylint: disable=too-many-ancestors
    """ Detail page model """
    introduction = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Entrer votre introduction",
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Choisir votre image",
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Entrer votre description",
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        abstract = True


class DigitalisationPage(DetailPage):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Digitalisation Page"


class MissionPage(DetailPage):  # pylint: disable=too-many-ancestors
    """The Mission Page model """
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        InlinePanel("related_items", label="Mission items"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Mission Page"


class MissionPageRelatedItem(Orderable):
    """ The related item to Mission for Newrai page"""
    page = ParentalKey(
        MissionPage, on_delete=models.CASCADE, related_name="related_items"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("icon"),
    ]


class MissionPageRelatedItemForHome(Orderable):
    """ The related item to Mission for Home page"""
    page = ParentalKey(
        HomePage, on_delete=models.CASCADE,
        related_name="related_items_for_home"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("icon"),
    ]


class ProjectPage(DetailPage):  # pylint: disable=too-many-ancestors
    """The Project Page model """
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Project Page"


class VisionPage(DetailPage):  # pylint: disable=too-many-ancestors
    """The Project Page model """

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Vision Page"


class TetstimonialPage(Page):  # pylint: disable=too-many-ancestors
    """Testimonial model"""
    content_panels = Page.content_panels + [
        InlinePanel("testtimonial_items", label="Testimonial items"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Tetstimonial Page"


class TetstimonialPageRelatedItem(Orderable):
    """The Related Item of Tetstemonial page"""
    page = ParentalKey(
        TetstimonialPage, on_delete=models.CASCADE,
        related_name="testtimonial_items",
    )
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    panels = [
        FieldPanel("image"),
        FieldPanel("name"),
        FieldPanel("role"),
        FieldPanel("description"),
    ]
