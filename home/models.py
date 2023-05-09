from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from offer.models import DigitalOfferPage


@register_snippet
class Home(models.Model):
    """ The home model"""
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    image = models.ForeignKey(
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

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
                FieldPanel("image"),
                FieldPanel("description"),
            ]
        )
    ]

    def __str__(self) -> str:
        return str(self.title)


class HomePageHomePlacement(Orderable, models.Model):
    """ The home placement """
    page = ParentalKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="home_placements"
    )
    home = models.ForeignKey(
        "home.Home",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('home'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.home.title

    class Meta(Orderable.Meta):  # pylint: disable=too-few-public-methods
        """ The meta model"""
        verbose_name = "home placement"
        verbose_name_plural = "home placements"


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

    # ====================== Project Section Model ============================
    home_image_project = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    home_title_project = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter le titre du projet",
    )

    home_desc_project = RichTextField(blank=True)

    # ===================== Novelty Section model ==============================
    home_image_novelty = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    home_title_novelty = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ajouter le titre de noveauté",
    )
    home_desc_novelty = RichTextField(blank=True)

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

    content_panels = Page.content_panels + [
        # ======= Hero Section panel
        InlinePanel("home_placements", label="Home"),
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
                FieldPanel("first_intro_mission", heading="First Intro"),
                FieldPanel("first_desc_mission", heading="First Desc"),
                FieldPanel("second_intro_mission", heading="Second Intro"),
                FieldPanel("second_desc_mission", heading="Second Desc"),
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

        # ========= Project Section Panel

        MultiFieldPanel(
            [
                FieldPanel("home_image_project", heading="Image"),
                FieldPanel("home_title_project", heading="Title"),
                FieldPanel("home_desc_project", heading="Description"),
            ],
            heading="Project",
        ),

        # ========= Novelty Section Panel
        MultiFieldPanel(
            [
                FieldPanel("home_image_novelty", heading="Image"),
                FieldPanel("home_title_novelty", heading="Title"),
                FieldPanel("home_desc_novelty", heading="Description"),
            ],
            heading="Novelty",
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


class DigitalisationPage(Page):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """
    introduction = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Entrer votre introduction',
    )
    logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Choisir votre image',
    )

    description = RichTextField(
        blank=True,
        null=True,
        help_text='Entrer votre description',
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Digitalisation Page"


class MissionPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Mission Page model """
    second_intro = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Entrer votre seconde introduction"
    )
    second_desc = RichTextField(
        blank=True,
        null=True,
        help_text="Entrer votre seconde description"
    )

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("image"),
        FieldPanel("introduction"),
        FieldPanel("description"),
        FieldPanel("second_intro"),
        FieldPanel("second_desc"),

    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Mission Page"


class ProjectPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Project Page model """

    content_panels = Page.content_panels + [
        # FieldPanel("introduction"),
        FieldPanel("logo"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Project Page"


class VisionPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Project Page model """

    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Vision Page"


class ContactPage(DigitalisationPage):  # pylint: disable=too-many-ancestors
    """The Digitalisation Page model """
    name = models.CharField(
        max_length=255,
        blank=True,
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
    entreprise = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    fonction = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    message = RichTextField(
        blank=True,
        null=True,
    )
    conatct_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text='Choisir votre contact image',
    )
    content_panels = Page.content_panels + [
        FieldPanel("logo"),
        FieldPanel("introduction"),
        FieldPanel("description"),
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("object"),
        FieldPanel("entreprise"),
        FieldPanel("fonction"),
        FieldPanel("message"),
        FieldPanel("conatct_image"),
    ]

    class Meta:  # pylint: disable=too-few-public-methods
        """The meta class"""
        verbose_name = "Contact Page"
