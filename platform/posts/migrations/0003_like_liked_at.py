# Generated by Django 5.0.2 on 2024-02-24 22:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='liked_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]