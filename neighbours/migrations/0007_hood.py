# Generated by Django 4.0.3 on 2022-04-19 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbours', '0006_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbours.neighborhood')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
