# Generated by Django 3.0.4 on 2020-05-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0031_auto_20200504_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
