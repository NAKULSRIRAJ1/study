# Generated by Django 5.1.1 on 2024-10-30 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_book_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
