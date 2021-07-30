# Generated by Django 3.2.4 on 2021-07-30 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_project', '0015_auto_20210729_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ManyToManyField(related_name='project_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='reporter',
            field=models.ManyToManyField(blank=True, null=True, related_name='project_reported', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Organization name')),
                ('description', models.TextField(verbose_name='Organization description')),
                ('member', models.ManyToManyField(related_name='org_joined', to=settings.AUTH_USER_MODEL, verbose_name='Members')),
                ('owner', models.ManyToManyField(related_name='org_owned', to=settings.AUTH_USER_MODEL, verbose_name='Organization owner')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='base_project.organization'),
        ),
    ]