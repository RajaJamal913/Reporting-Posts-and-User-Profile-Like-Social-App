# Generated by Django 5.0.6 on 2024-08-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_report_report_type_report_user_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='post',
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('post', 'Post'), ('user_profile', 'User Profile')], default='user_profile', max_length=20),
        ),
    ]
