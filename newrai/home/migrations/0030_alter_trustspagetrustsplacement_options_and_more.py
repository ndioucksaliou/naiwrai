# Generated by Django 4.1.9 on 2023-05-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_digitalisationpage_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trustspagetrustsplacement',
            options={'ordering': ['sort_order'], 'verbose_name': 'trust placement', 'verbose_name_plural': 'trust placements'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='trust_intro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
