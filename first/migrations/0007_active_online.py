# Generated by Django 2.2.2 on 2020-06-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20200620_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]