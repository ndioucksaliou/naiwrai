# Generated by Django 4.1.7 on 2023-04-27 10:15

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("home", "0013_home_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="app_desc",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="app_intro",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="app_title",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="cloud_desc",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="cloud_intro",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="cloud_left_image",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="cloud_right_image",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="cloud_second_right_image",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="cloud_title",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="desc_of_digital_section",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="digital_approch_title",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="digital_revolution_title",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="digital_transition_title",
        ),
        migrations.RemoveField(
            model_name="digitalisationpage",
            name="first_intro_mission",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="global_approch_desc",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="global_approch_image",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="global_approch_intro",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="global_approch_small_text",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="global_approch_title",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="innovation_approch_desc",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="innovation_approch_image",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="innovation_approch_intro",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="innovation_approch_small_text",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="innovation_approch_title",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="transition_approch_desc",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="transition_approch_image",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="transition_approch_intro",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="transition_approch_small_text",
        ),
        migrations.RemoveField(
            model_name="missionpage",
            name="transition_approch_title",
        ),
        migrations.AddField(
            model_name="digitalisationpage",
            name="description",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Entrer votre description",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="digitalisationpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="Choisir votre image",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="missionpage",
            name="second_desc",
            field=wagtail.fields.RichTextField(
                blank=True,
                help_text="Entrer votre seconde description",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="missionpage",
            name="second_intro",
            field=models.CharField(
                blank=True,
                help_text="Entrer votre seconde introduction",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="digitalisationpage",
            name="introduction",
            field=models.CharField(
                help_text="Entrer votre introduction", max_length=255, null=True
            ),
        ),
    ]
