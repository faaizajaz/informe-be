# Generated by Django 3.2.4 on 2021-07-02 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_project', '0004_project_impact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='impact',
        ),
    ]