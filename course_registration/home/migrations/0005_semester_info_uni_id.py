# Generated by Django 4.2.6 on 2024-02-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_semester_info_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester_info',
            name='uni_id',
            field=models.IntegerField(default=0),
        ),
    ]
