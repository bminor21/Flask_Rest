# Generated by Django 2.2.2 on 2019-06-26 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_minute',
            new_name='time_minutes',
        ),
    ]