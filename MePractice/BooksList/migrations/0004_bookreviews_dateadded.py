# Generated by Django 5.1 on 2024-09-03 08:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksList', '0003_alter_bookreviews_review_alter_books_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreviews',
            name='DateAdded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
