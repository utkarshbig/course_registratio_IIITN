# Generated by Django 4.2.6 on 2024-02-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_database_remove_course_info_branch_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='roll_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
            ],
        ),
    ]
