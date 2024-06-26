# Generated by Django 3.2.4 on 2021-07-15 07:16

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base_project', '0006_remove_project_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_project.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='base_project.project'),
        ),
    ]
