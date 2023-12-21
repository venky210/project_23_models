from django.shortcuts import render

# Create your views here.
from app.models import *

def display_dept(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)


def display_emp(request):
    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'display_emp.html',d)


def insert_dept(request):
    d=int(input('enter deptno: '))
    dn=input('enter dname: ')
    l=input('enter loc: ')
    NDO=Dept.objects.get_or_create(dept_no=d,dname=dn,loc=l)[0]
    NDO.save()
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)


def insert_emp(request):
    e=int(input('enter empno: '))
    en=input('enter ename: ')
    j=input('enter job: ')
    h=input('enter hiredate: ')
    s=int(input('enter sal: '))
    c=int(input('enter comm: '))
    d=int(input('enter deptno: '))
    DO=Dept.objects.get(dept_no=d)
    NEO=Emp.objects.get_or_create(emp_no=e,ename=en,job=j,hiredate=h,sal=s,comm=c,dept_no=DO)[0]
    NEO.save()
    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'display_emp.html',d)
