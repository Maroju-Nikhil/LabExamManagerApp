# Generated by Django 3.1.6 on 2021-03-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_studentattend_taskreport_taskreportstudent_tasksession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='archive',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
