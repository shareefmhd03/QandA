# Generated by Django 3.2.5 on 2021-07-24 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('q_and_a', '0002_auto_20210724_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]
