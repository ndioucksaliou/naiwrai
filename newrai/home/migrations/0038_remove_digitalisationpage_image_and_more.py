# Generated by Django 4.1.9 on 2023-05-26 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_tetstimonialpage_tetstimonialpagerelateditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitalisationpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='digitalisationpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='missionpage',
            name='digitalisationpage_ptr',
        ),
        migrations.RemoveField(
            model_name='missionpagerelateditem',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='missionpagerelateditem',
            name='page',
        ),
        migrations.RemoveField(
            model_name='missionpagerelateditemforhome',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='missionpagerelateditemforhome',
            name='page',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='digitalisationpage_ptr',
        ),
        migrations.RemoveField(
            model_name='visionpage',
            name='digitalisationpage_ptr',
        ),
        migrations.AlterModelOptions(
            name='tetstimonialpage',
            options={'verbose_name': 'Tetstimonial Page'},
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
        migrations.DeleteModel(
            name='DigitalisationPage',
        ),
        migrations.DeleteModel(
            name='MissionPage',
        ),
        migrations.DeleteModel(
            name='MissionPageRelatedItem',
        ),
        migrations.DeleteModel(
            name='MissionPageRelatedItemForHome',
        ),
        migrations.DeleteModel(
            name='ProjectPage',
        ),
        migrations.DeleteModel(
            name='VisionPage',
        ),
    ]
