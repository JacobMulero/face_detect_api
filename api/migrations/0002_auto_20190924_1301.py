# Generated by Django 2.2.5 on 2019-09-24 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='callback_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.CharField(default='processing', max_length=100),
        ),
    ]
