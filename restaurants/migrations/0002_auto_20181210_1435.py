# Generated by Django 2.1.4 on 2018-12-10 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='stateOrProvince',
            new_name='state_or_province',
        ),
    ]
