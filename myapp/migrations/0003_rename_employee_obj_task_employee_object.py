# Generated by Django 5.0.3 on 2024-05-31 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_task_completion_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='employee_obj',
            new_name='employee_object',
        ),
    ]
