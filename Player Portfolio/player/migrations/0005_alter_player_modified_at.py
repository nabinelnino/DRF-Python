# Generated by Django 4.0.4 on 2022-05-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_player_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
