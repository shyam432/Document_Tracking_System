from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import *
from datetime import datetime
# Create your views here.
def Home(request):
    user = ""
    emp = ""
    if not request.user.is_staff and request.user.username:
        user = User.objects.get(username = request.user.username)
        emp = Employee.objects.get(user=user)
    d = {'emp': emp}
    return render(request,'carousel.html',d)

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')


def Admin_Sign(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                return redirect('home')
        except:
            pass
    return render(request,'admin_sign.html')


def Add_Employee(request):
    dept1=Department.objects.all()
    type1=Type.objects.all()
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        p=request.POST['pwd']
        d=request.POST['date']
        e=request.POST['email']
        m=request.POST['mobile']
        a=request.POST['add']
        de=request.POST['dept']
        t=request.POST['type']
        g=request.POST['gen']
        dept=Department.objects.get(dept=de)
        type=Type.objects.get(type=t)
        user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        Employee.objects.create(user=user,d_birth=d,type=type,department=dept,mobile=m,add=a,gen=g)
    d={'type':type1,'dept':dept1}
    return render(request,'add_employee.html',d)


def viewdata(request):
    data1=Employee.objects.all()
    d={'data1':data1}
    return render(request,'view.html',d)

def Logout(request):
    logout(request)
    return redirect('home')


def employee_login(request):
    error=False
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error=True
    d={'error':error}
    return render(request,'loginemployee.html',d)


def uploadfile(request):
    user = User.objects.get(username=request.user.username)
    emp = Employee.objects.filter(user=user).first()
    type=Type.objects.all()
    dept=Department.objects.all()
    error=False
    if request.method=='POST':
         s=request.POST['sub']
         d=request.POST['des']
         t=request.POST['type']
         de=request.POST['dept']
         f=request.FILES['file']
         type1=Type.objects.filter(type=t).first()
         dept1=Department.objects.filter(dept=de).first()
         user=User.objects.filter(username=request.user.username).first()
         emp=Employee.objects.filter(user=user).first()
         sta=Status.objects.all()
         if type1.id > emp.type.id:
             sta = Status.objects.get(status="pending")
         else:
             sta = Status.objects.get(status="No")
         upload=Uploadfile.objects.create(status=sta,sub=s,des=d,type=type1,department=dept1,file=f,emp=emp)
         error=True
    d={'type':type,'dept':dept,'emp': emp,'error':error}
    return render(request,'uploadfile.html',d)


def viewfile(request):
    emp1=Uploadfile.objects.all()
    user = User.objects.get(username=request.user.username)
    emp_type = Employee.objects.get(user=user)
    d={'data1': emp1,'emp':emp_type}
    return render(request,'viewfile.html',d)


def viewstatus(request):
    user = User.objects.get(username=request.user.username)
    emp = Employee.objects.filter(user=user).first()
    data1=Uploadfile.objects.all()
    d={'data':data1,'emp': emp}
    return render(request,'viewstatus.html',d)


def change_password(request):
    user = User.objects.get(username=request.user.username)
    emp = Employee.objects.get(user=user)
    error=""
    if request.method=="POST":
        n = request.POST['New']
        c = request.POST['confirm']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="yes"
        else:
            error="not"
    d = {'emp': emp,'error':error}
    return render(request,'change_password.html',d)


def delete_file(request,pid):
    data=Uploadfile.objects.get(id=pid)
    data.delete()
    return redirect('viewstatus')


def change_status(request,pid):
    upload = Uploadfile.objects.get(id=pid)
    user = User.objects.get(username=request.user.username)
    emp_type = Employee.objects.get(user=user)
    error = ""
    if request.method=="POST":
        i = request.POST['id']
        s = request.POST['status']
        if emp_type.type.type == "Deputy Engineer":
            sta = Status.objects.get(status=s)
            upload.status = sta
            upload.save()
            error = "not"

        if emp_type.type.type == "Executive Engineer":
            sta = Status.objects.get(status=s)
            upload.status = sta
            upload.save()
            error = "yes"
    d = {'error':error,'data':upload,'emp':emp_type}
    return render(request,'change_status.html',d)


def edit_employee(request,pid):
    data=Employee.objects.get(id=pid)
    dept = Department.objects.all()
    type = Type.objects.all()
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        a=request.POST['add']
        m=request.POST['mobile']
        e=request.POST['email']
        try:
            t=request.POST['type']
            data.type = t
            data.save()
        except:
            pass
        try:
            g=request.POST['gen']
            data.gen=g
            data.save()
        except:
            pass
        try:
            d=request.POST['department']
            data.department=d
            data.save()
        except:
            pass
        data.user.first_name=f
        data.user.last_name=l
        data.user.username=u
        data.user.email=e
        data.add=a
        data.mobile=m
        b = request.POST['date1']
        if b:
            try:
                data.d_birth = b
                data.save()
            except:
                pass
        else:
            pass
        data.user.save()
        data.save()
    d={'data':data,'dept':dept,'type':type}
    return render(request,'editview.html',d)


def delete_view(request,pid):
    type=Employee.objects.get(id=pid)
    type.delete()
    return redirect('viewdata')

