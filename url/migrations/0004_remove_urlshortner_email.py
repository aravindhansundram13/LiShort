# Generated by Django 2.2.5 on 2019-09-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0003_auto_20190927_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshortner',
            name='email',
        ),
    ]
