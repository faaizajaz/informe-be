# Generated by Django 3.2.4 on 2021-07-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_last_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_org',
            field=models.IntegerField(default=None, verbose_name='Last organization active'),
        ),
    ]
