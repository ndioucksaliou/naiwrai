from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey


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
        on_delete=models.CASCADE,
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
        on_delete=models.CASCADE,
        related_name="home_placements"
    )
    home = models.ForeignKey(
        "home.Home",
        on_delete=models.CASCADE,
        related_name='+',
    )

    panels = [
        FieldPanel('home'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.home.title

    class Meta(Orderable.Meta): # pylint: disable=too-few-public-methods
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
    # ==================== Offer Section Model ==================

    # ===================== Mission Section Model =========================
    home_image_mission = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
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

    # ====================== Project Section Model =============================
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
        FieldPanel("home_description"),
        FieldPanel("home_image_logo"),

        # ======= Mission Section Pannel
        FieldPanel("home_image_mission"),
        FieldPanel("first_intro_mission"),
        FieldPanel("first_desc_mission"),
        FieldPanel("second_intro_mission"),
        FieldPanel("second_desc_mission"),

        # ========= Vision Section Panel
        FieldPanel("home_image_vision"),
        FieldPanel("home_title_vision"),
        FieldPanel("home_intro_vision"),
        FieldPanel("home_desc_vision"),

        # ========= Project Section Panel
        FieldPanel("home_image_project"),
        FieldPanel("home_title_project"),
        FieldPanel("home_desc_project"),

        # ========= Novelty Section Panel
        FieldPanel("home_image_novelty"),
        FieldPanel("home_title_novelty"),
        FieldPanel("home_desc_novelty"),

        # ========= Commitment Section Panel
        FieldPanel("home_image_commitment"),
        FieldPanel("home_title_commitment"),
        FieldPanel("home_desc_commitment"),

        InlinePanel("home_placements", label="Home"),
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

    desc_of_digital_section = RichTextField(
        blank=True,
        null=True,
    )
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
    cloud_desc = RichTextField(
        blank=True,
        null=True,
    )
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
    app_desc = RichTextField(
        blank=True,
        null=True,
    )
    first_intro_mission = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="1ère introduction de l'offre",
    )
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
    innovation_approch_desc = RichTextField(
        blank=True,
        null=True,
    )
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
    global_approch_desc = RichTextField(
        blank=True,
        null=True,
    )
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
    transition_approch_desc = RichTextField(
        blank=True,
        null=True,
    )
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
    message = RichTextField(
        max_length=255,
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
