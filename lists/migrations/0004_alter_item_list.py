# Generated by Django 5.0.2 on 2024-03-08 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_item_list_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
        ),
    ]
