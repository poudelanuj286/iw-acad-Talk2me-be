# Generated by Django 2.2 on 2020-09-01 07:14

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20200823_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
