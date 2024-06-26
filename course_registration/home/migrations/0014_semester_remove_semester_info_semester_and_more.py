# Generated by Django 4.2.6 on 2024-02-18 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_course_info_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='semester_info',
            name='semester',
        ),
        migrations.AddField(
            model_name='semester_info',
            name='sem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.semester'),
        ),
    ]
