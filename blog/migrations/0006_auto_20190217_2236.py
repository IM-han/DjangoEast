# Generated by Django 2.1.5 on 2019-02-17 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190217_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='dd',
        ),
    ]