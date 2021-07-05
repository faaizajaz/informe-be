# Generated by Django 3.2.4 on 2021-07-02 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impact', '0002_alter_impact_id'),
        ('base_project', '0003_remove_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='impact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='impact.impact'),
        ),
    ]
