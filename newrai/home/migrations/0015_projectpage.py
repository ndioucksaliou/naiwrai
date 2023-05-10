# Generated by Django 4.1.7 on 2023-04-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_remove_digitalisationpage_app_desc_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectPage",
            fields=[
                (
                    "digitalisationpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="home.digitalisationpage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Project Page",
            },
            bases=("home.digitalisationpage",),
        ),
    ]