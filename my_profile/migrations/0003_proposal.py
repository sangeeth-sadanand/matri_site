# Generated by Django 2.2.5 on 2019-12-24 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_interestedprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(default=' ', max_length=15)),
                ('whatsapp_number', models.CharField(default=' ', max_length=15)),
                ('message', models.CharField(default=' ', max_length=250)),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('proposal_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposal_to', to='my_profile.UserProfile')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.UserProfile')),
            ],
            options={
                'db_table': 'Proposal',
            },
        ),
    ]
