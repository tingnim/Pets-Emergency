# Generated by Django 3.0.8 on 2020-07-10 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petsemergency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pets',
            old_name='content',
            new_name='pcontent',
        ),
    ]
