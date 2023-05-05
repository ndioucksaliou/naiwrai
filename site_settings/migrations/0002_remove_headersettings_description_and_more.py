# Generated by Django 4.1.7 on 2023-05-05 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("site_settings", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="headersettings",
            name="description",
        ),
        migrations.RemoveField(
            model_name="headersettings",
            name="image",
        ),
        migrations.AddField(
            model_name="headersettings",
            name="logo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
