# Generated by Django 5.0.2 on 2024-05-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_author_options_alter_book_instance_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
