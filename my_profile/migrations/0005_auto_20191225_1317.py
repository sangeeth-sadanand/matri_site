# Generated by Django 2.2.5 on 2019-12-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0004_married'),
    ]

    operations = [
        migrations.RenameField(
            model_name='married',
            old_name='he',
            new_name='user_profile',
        ),
        migrations.RemoveField(
            model_name='married',
            name='she',
        ),
        migrations.AddField(
            model_name='married',
            name='met_here',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='married',
            name='would_be',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
