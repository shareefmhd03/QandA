# Generated by Django 3.2.5 on 2021-07-30 11:57

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_alter_tutorial_turorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='turorial',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
