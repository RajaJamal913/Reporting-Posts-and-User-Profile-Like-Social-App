# Generated by Django 5.0.6 on 2024-08-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_remove_userprofile_ban_until_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ban_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='report_count',
            field=models.IntegerField(default=0),
        ),
    ]