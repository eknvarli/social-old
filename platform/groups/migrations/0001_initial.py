# Generated by Django 5.0.2 on 2024-02-29 20:44

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('is_public', models.BooleanField(default=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'group',
            },
        ),
    ]
