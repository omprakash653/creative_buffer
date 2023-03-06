from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import loader


def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home2.html", {'emps': emps})


def add_emp(request):
    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")

        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        e = Emp()

        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone

        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
        
    return render(request, "emp/add_emp.html", {})


def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    
    return render(request, "emp/home.html", {})


def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request, "emp/update_emp.html", {
        'emp': emp
    })


def do_update_emp(request, emp_id):
    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")

        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Emp.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone

        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
    
    return render(request, "emp/home.html", {})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('login successfully!')
            return redirect('home/')
        else:
            messages.error(request,'username or password not correct')
            print('something is wrong..')
            return redirect('login')
    else:
        return render(request, 'emp/login.html')

def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request)
            messages.success(request, '(Registration Successful!)')
            return redirect('login')    
    store = {'form':form}
    return render(request, 'emp/signup.html', store)


def user_logout(request):
    logout(request)
    messages.success(request,'You logged Out successfully.')
    return redirect("home/")


