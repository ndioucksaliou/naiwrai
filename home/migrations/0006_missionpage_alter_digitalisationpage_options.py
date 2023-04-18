# Generated by Django 4.1.7 on 2023-04-18 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_digitalisationpage"),
    ]

    operations = [
        migrations.CreateModel(
            name="MissionPage",
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
                "verbose_name": "Mission Page",
            },
            bases=("home.digitalisationpage",),
        ),
        migrations.AlterModelOptions(
            name="digitalisationpage",
            options={"verbose_name": "Digitalisation Page"},
        ),
    ]
