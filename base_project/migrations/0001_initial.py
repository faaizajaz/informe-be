# Generated by Django 3.2.4 on 2021-06-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=1000, verbose_name='Short description of project')),
                ('long_description', models.TextField(verbose_name='Long description of project')),
            ],
        ),
    ]