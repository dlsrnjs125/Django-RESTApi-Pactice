# Generated by Django 4.2.19 on 2025-03-04 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0003_books_stock'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.books', verbose_name='Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users', verbose_name='User')),
            ],
            options={
                'db_table': 'Orders',
                'ordering': ['-created_at'],
            },
        ),
    ]
