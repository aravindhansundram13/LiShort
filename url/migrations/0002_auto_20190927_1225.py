# Generated by Django 2.2.5 on 2019-09-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='email',
            field=models.EmailField(default='None', max_length=254),
        ),
        migrations.AlterField(
            model_name='urlshortner',
            name='shorted_url',
            field=models.CharField(max_length=50),
        ),
    ]
