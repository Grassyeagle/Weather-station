# Generated by Django 2.1.5 on 2019-01-23 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temperature',
            old_name='temperature',
            new_name='celcius',
        ),
    ]
