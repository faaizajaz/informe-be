# Generated by Django 3.2.4 on 2022-02-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_project', '0018_organization_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='org_profile-pics'),
        ),
    ]
