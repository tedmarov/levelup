# Generated by Django 3.1.6 on 2021-02-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(default='Unknown', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
