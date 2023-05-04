from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class ApplicationIndexPage(Page):  # pylint: disable=too-many-ancestors
    """Application Index Page Model"""
    def get_context(self, request):
        context = super().get_context(request)
        all_apps = self.get_children().live().order_by("-first_published_at")
        context["apps"] = all_apps
        return context


class ApplicationPage(Page):  # pylint: disable=too-many-ancestors
    """Application Page Model"""
    name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    description = RichTextField(
        blank=True,
        null=True,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.CASCADE, related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]
