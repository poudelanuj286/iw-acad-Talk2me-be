# Generated by Django 2.2 on 2020-08-31 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200831_0612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='username',
            new_name='name',
        ),
    ]
