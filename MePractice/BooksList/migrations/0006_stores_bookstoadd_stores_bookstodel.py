# Generated by Django 5.1 on 2024-09-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksList', '0005_books_date_added_stores_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='booksToAdd',
            field=models.ManyToManyField(related_name='Temp_ToAdd', to='BooksList.books'),
        ),
        migrations.AddField(
            model_name='stores',
            name='booksToDel',
            field=models.ManyToManyField(related_name='Temp_ToRemove', to='BooksList.books'),
        ),
    ]
