# Generated by Django 3.1.1 on 2020-10-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0002_auto_20201028_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('title', 'number', 'major')},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='title',
        ),
    ]
