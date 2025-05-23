# Generated by Django 5.1.4 on 2025-04-30 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0011_paper_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='checked_papers/')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_of_paper', to='paper.paper')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_of_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
