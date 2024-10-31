# Generated by Django 5.1.2 on 2024-10-30 16:31

import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='vlog-media')),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
                ('desc', models.CharField(max_length=90)),
                ('pinned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image-project')),
                ('desc', models.TextField(max_length=1000)),
                ('belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]