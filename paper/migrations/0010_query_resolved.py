# Generated by Django 5.1.4 on 2025-04-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0009_remove_query_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
