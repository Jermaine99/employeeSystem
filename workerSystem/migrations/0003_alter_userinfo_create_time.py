# Generated by Django 3.2.5 on 2022-04-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerSystem', '0002_auto_20220408_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]
