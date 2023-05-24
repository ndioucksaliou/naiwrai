# Generated by Django 4.1.9 on 2023-05-23 11:10

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0005_alter_headersettings_carousel_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headersettings',
            name='carousel_item',
            field=wagtail.fields.StreamField([('list_items', wagtail.blocks.StructBlock([('description', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))]))], blank=True, null=True, use_json_field=True),
        ),
    ]