# Generated by Django 3.2.4 on 2021-07-26 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_project', '0014_alter_project_reporter'),
        ('indicator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicator',
            name='long_description',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='short_description',
        ),
        migrations.AddField(
            model_name='indicator',
            name='description',
            field=models.TextField(null=True, verbose_name='Description of indicator'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicator', to='base_project.item', verbose_name='Parent item'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='name',
            field=models.CharField(max_length=1000, null=True, verbose_name='Name of indicator'),
        ),
        migrations.CreateModel(
            name='IndicatorEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True, verbose_name='Name of evidence')),
                ('description', models.TextField(null=True, verbose_name='Description of evidence')),
                ('indicator', models.ManyToManyField(null=True, related_name='indicator', to='indicator.Indicator')),
            ],
        ),
    ]