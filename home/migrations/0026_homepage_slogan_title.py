# Generated by Django 4.1.7 on 2023-05-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0025_rename_youtube_homepage_youtube_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="slogan_title",
            field=models.CharField(
                blank=True,
                help_text="Ajouter le titre du slogan",
                max_length=255,
                null=True,
            ),
        ),
    ]
