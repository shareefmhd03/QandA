# Generated by Django 3.2.5 on 2021-07-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q_and_a', '0025_question_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='solved',
            field=models.BooleanField(default=False),
        ),
    ]
