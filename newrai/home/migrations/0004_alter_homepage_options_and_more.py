# Generated by Django 4.1.7 on 2023-04-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_image_banner_homepage_sub_banner_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Home Page"},
        ),
        migrations.RenameField(
            model_name="homepage",
            old_name="sub_banner",
            new_name="home_description",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="image_banner",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="text_banner",
        ),
    ]