# Generated by Django 4.2 on 2024-10-24 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecordhashhistory',
            name='previous_hash',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]