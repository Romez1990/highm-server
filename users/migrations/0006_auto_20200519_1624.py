# Generated by Django 3.0.5 on 2020-05-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_unregistereduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unregistereduser',
            old_name='code',
            new_name='registration_code',
        ),
    ]