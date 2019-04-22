# Generated by Django 2.0.8 on 2019-04-22 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='菜单名称')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单链接')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单图标')),
            ],
            options={
                'verbose_name': '菜单栏',
                'verbose_name_plural': '菜单栏',
            },
        ),
    ]
