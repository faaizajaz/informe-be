# Generated by Django 3.2.4 on 2021-08-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_project', '0017_alter_project_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile-pics'),
        ),
    ]
