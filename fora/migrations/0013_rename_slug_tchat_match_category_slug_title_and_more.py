# Generated by Django 5.0.4 on 2024-05-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fora', '0012_delete_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tchat_match_category',
            old_name='slug',
            new_name='slug_title',
        ),
        migrations.AddField(
            model_name='tchat_match_category',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tchat_match_category',
            name='slug_country',
            field=models.SlugField(blank=True, max_length=600, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tchat_match_category',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
