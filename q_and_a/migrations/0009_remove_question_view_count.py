# Generated by Django 3.2.5 on 2021-08-23 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('q_and_a', '0008_alter_question_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='view_count',
        ),
    ]
