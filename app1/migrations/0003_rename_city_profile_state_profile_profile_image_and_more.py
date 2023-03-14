# Generated by Django 4.1.7 on 2023-03-03 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_roles_profile_bio_profile_roles_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city',
            new_name='state',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]