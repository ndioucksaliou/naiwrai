# Generated by Django 4.1.9 on 2023-05-24 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_remove_homepage_home_desc_novelty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagehomeplacement',
            name='home',
        ),
        migrations.RemoveField(
            model_name='homepagehomeplacement',
            name='page',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.DeleteModel(
            name='HomePageHomePlacement',
        ),
    ]