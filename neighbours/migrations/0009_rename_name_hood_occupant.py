# Generated by Django 4.0.3 on 2022-04-19 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0008_alter_hood_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hood',
            old_name='name',
            new_name='occupant',
        ),
    ]
