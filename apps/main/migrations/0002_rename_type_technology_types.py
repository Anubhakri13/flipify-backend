# Generated by Django 4.1.2 on 2022-10-19 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technology',
            old_name='type',
            new_name='types',
        ),
    ]
