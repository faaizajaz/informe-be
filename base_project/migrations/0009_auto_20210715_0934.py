# Generated by Django 3.2.4 on 2021-07-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_project', '0008_project_level_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_type',
        ),
        migrations.AddField(
            model_name='item',
            name='is_project',
            field=models.BooleanField(default=False),
        ),
    ]
