# Generated by Django 4.1.7 on 2023-04-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_remove_homepage_home_commitment_logo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="home_title_mission",
            field=models.CharField(
                blank=True,
                help_text="Ajouter le titre de vision",
                max_length=255,
                null=True,
            ),
        ),
    ]
