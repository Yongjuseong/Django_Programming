# Generated by Django 3.1.1 on 2020-10-21 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION'),
        ),
    ]
