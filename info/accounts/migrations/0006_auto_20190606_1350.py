# Generated by Django 2.2 on 2019-06-06 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190606_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='Firstname',
            new_name='Fullname',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='Lastname',
        ),
    ]
