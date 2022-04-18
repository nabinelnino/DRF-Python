# Generated by Django 4.0.4 on 2022-05-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='first_name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='nationality',
            field=models.CharField(default='Nepal', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='place_of_birth',
            field=models.CharField(default='Nepal', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]