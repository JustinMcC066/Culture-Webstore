# Generated by Django 3.1.4 on 2021-01-15 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='soundcloud_embed',
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
    ]
