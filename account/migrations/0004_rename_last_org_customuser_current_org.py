# Generated by Django 3.2.4 on 2021-07-30 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_last_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='last_org',
            new_name='current_org',
        ),
    ]
