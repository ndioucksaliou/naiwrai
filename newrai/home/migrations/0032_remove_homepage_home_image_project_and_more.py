# Generated by Django 4.1.9 on 2023-05-24 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_whychoosenewrai_homepage_why_choose_newrai_intro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='home_image_project',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='home_title_project',
        ),
    ]
