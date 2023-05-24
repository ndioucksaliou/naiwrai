# Generated by Django 4.1.9 on 2023-05-24 11:15

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0030_alter_trustspagetrustsplacement_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseNewrai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='why_choose_newrai_intro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='WhyChooseNewraiPageChooseNewraiPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='whychoosenewrai_items', to='home.homepage')),
                ('whychoosenewrai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.whychoosenewrai')),
            ],
            options={
                'verbose_name': 'whychoosenewrai placement',
                'verbose_name_plural': 'whychoosenewrai placements',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
