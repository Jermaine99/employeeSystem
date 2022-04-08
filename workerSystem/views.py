from django.shortcuts import render, HttpResponse, redirect
from django import forms
from workerSystem import models
# Create your views here.


def department(request):
    """
    models.Department.objects.create(tittle="技术部门")
    models.Department.objects.create(tittle="营销部门")
    models.Department.objects.create(tittle="运营部门")
    """
    if request.method == "GET":
        departments = models.Department.objects.all()
        return render(request, 'department.html', {"departments": departments})



def department_add(request):
    if request.method == "GET":
        return render(request, 'add.html')
    tittle = request.POST.get("tittle")
    models.Department.objects.create(tittle=tittle)
    return redirect("/department/")


def department_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/department/')


def department_edit(request, nid):
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'edit.html', {"row_object": row_object})
    tittle = request.POST.get("tittle")
    models.Department.objects.filter(id=nid).update(tittle=tittle)
    return redirect("/department/")


class UserForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name",  "account", "password", "age", "salary", "create_time", "sex", "depart"]

        # 原始方法通过 widgets 修改样式
        # widgets = {
        #      "name": forms.TextInput(attrs={"class": "form_control"}),
        #      "account": forms.TextInput(attrs={"class": "form_control"}),
        #      "password": forms.PasswordInput(attrs={"class": "form_control"})
        #      "name": forms.TextInput(attrs={"class": "form_control"}),
        #      "account": forms.TextInput(attrs={"class": "form_control"}),
        #
        # }

    # 进阶方法循环遍历fields 修改widgets样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control"}


def user(request):
    if request.method == "GET":
        users = models.UserInfo.objects.all()

        # for user in users:
        #    print(user.id, user.create_time.strftime("%Y-%m-%d"), user.sex, user.get_sex_display(), user.depart.tittle)
        return render(request, 'user.html', {"users": users})


def user_add(request):
    if request.method == "GET":
        depart = models.Department.objects.all()
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'department': models.Department.objects.all(),
        }
        return render(request, 'user_add.html', context)
    name = request.POST.get("name")
    account = request.POST.get("account")
    password = request.POST.get("password")
    age = request.POST.get("age")
    salary = request.POST.get("salary")
    create_time = request.POST.get("create_time")
    sex = request.POST.get("sex")
    depart = request.POST.get("depart")

    models.UserInfo.objects.create(name=name, account=account, password=password, age=age,
                                   salary=salary, create_time=create_time,
                                   sex=sex, depart_id=depart)

    return redirect("/user/list/")


def user_add_model_form(request):

    if request.method == "GET":
        user_form = UserForm()
        return render(request, 'user_add_model_form.html', {"user_form": user_form})

    # 对用户输入的数据进行校验：
    form = UserForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 如果校验成功 保存
        form.save()
        return redirect("/user/list/")
    else:
        # 校验失败 显示错误信息
        print(form.errors)
        return render(request, 'user_add_model_form.html', {"user_form": form})


def user_edit(request, nid):

    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserForm(instance=row_object)
        return render(request, 'user_edit.html', {"user_form": form})

    form = UserForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # print(form.cleaned_data)
        # 如果校验成功 保存
        # form 是用户输入的字段
        # form.instance.字段名 = 值  添加不需要用户输入的字段
        form.save()
        return redirect("/user/list/")
    else:
        # 校验失败 显示错误信息
        print(form.errors)
        return render(request, 'user_add_model_form.html', {"user_form": form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
