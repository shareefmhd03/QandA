# Generated by Django 3.2.5 on 2021-07-31 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('q_and_a', '0026_alter_question_solved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='is_solved',
            new_name='is_solution',
        ),
    ]
