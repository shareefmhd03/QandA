# Generated by Django 3.2.5 on 2021-09-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0009_solved_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengetopic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
