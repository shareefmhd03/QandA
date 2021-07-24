# Generated by Django 3.2.5 on 2021-07-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('q_and_a', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='q_and_a.answer'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_desc',
            field=models.TextField(blank=True),
        ),
    ]
