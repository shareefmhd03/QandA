# Generated by Django 3.2.5 on 2021-07-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
