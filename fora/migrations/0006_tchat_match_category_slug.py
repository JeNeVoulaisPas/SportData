# Generated by Django 5.0.4 on 2024-04-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fora', '0005_alter_tchat_match_comment_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='tchat_match_category',
            name='slug',
            field=models.SlugField(blank=True, max_length=600, unique=True),
        ),
    ]
