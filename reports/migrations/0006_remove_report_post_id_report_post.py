# Generated by Django 5.0.6 on 2024-08-20 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('reports', '0005_remove_report_post_report_post_id_alter_report_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='post_id',
        ),
        migrations.AddField(
            model_name='report',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
