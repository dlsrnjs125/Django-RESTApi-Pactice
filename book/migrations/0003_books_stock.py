# Generated by Django 4.2.19 on 2025-03-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_books_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock'),
        ),
    ]
