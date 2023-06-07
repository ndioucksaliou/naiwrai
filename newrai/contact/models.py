from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)


class FormField(AbstractFormField, models.Model):
    """ Form Field model """
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
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


class ContactPage(AbstractEmailForm):  # pylint: disable=too-many-ancestors
    """ Contact Page model """
    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    introduction = RichTextField(blank=True)
    desc = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('introduction'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('desc'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
