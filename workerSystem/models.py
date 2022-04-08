from django.db import models

# Create your models here.


class Department(models.Model):
    """部门表"""

    tittle = models.CharField(verbose_name="部门标题", max_length=32)

    def __str__(self):
        return self.tittle


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    account = models.CharField(verbose_name="账号", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    salary = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间", )
    create_time = models.DateField(verbose_name="入职时间", )
    # 在Django中做约束
    gender_choices = (
        (1, "男"),
        (0, "女")
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    # 无约束
    # did = models.BigIntegerField(verbose_name="部门ID")  # 需要部门表ID的约束

    # 有约束
    # 1.部门表某列被删除，关联的员工表也被删除
    # depart = models.ForeignKey(verbose_name="部门ID", to="Department", to_field="id", on_delete=models.CASCADE())
    # 2.部门表删除， 关联部门ID 为 NONE
    depart = models.ForeignKey(verbose_name="部门ID", to="Department", to_field="id", on_delete=models.SET_NULL, null=True)
