# Generated by Django 4.2.4 on 2023-08-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_book_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=3, null=True),
        ),
    ]
