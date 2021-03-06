# Generated by Django 3.2.5 on 2022-04-06 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=32, verbose_name='部门标题')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('account', models.CharField(max_length=16, verbose_name='账号')),
                ('password', models.CharField(max_length=16, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额')),
                ('create_time', models.DateTimeField(verbose_name='入职时间')),
                ('sex', models.CharField(choices=[(1, '男'), (0, '女')], max_length=16, verbose_name='性别')),
                ('depart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workerSystem.department', verbose_name='部门ID')),
            ],
        ),
    ]
