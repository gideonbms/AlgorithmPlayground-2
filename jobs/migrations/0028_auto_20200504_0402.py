# Generated by Django 3.0.4 on 2020-05-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0027_auto_20200504_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Applicant',
        ),
    ]
