# Generated by Django 5.0.4 on 2024-05-02 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fora', '0011_remove_post_categories_remove_comment_replies_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='author',
        ),
    ]
