# Generated by Django 5.0.4 on 2024-04-29 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fora', '0003_tchat_match_category_tchat_match_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tchat_match_comment',
            name='categorie',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='fora.tchat_match_category'),
        ),
    ]
