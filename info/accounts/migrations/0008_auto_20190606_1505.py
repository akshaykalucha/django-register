# Generated by Django 2.2 on 2019-06-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190606_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='Fullname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
