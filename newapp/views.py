from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from newapp.forms import loginform, stockform
from newapp.models import Login, stock


# Create your views here.

def mainpage(request):
    return render(request,"index.html")

def adminpage(request):
    return render(request,'admin.html')

def user(request):
    return render(request,'user.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_customer:
                return redirect('user')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'log-in.html')

def register(request):
    u_form=loginform()
    if request.method=='POST':
        u_form=loginform(request.POST,request.FILES)
        if u_form.is_valid():
            user=u_form.save(commit=False)
            user.is_customer=True
            user.save()
            messages.info(request,'Registration Successfully')
            return redirect('loginpage')
    return render(request,'register.html',{'u_form':u_form})

def user_view(request):
    data= Login.objects.filter(is_customer=True)
    return render(request,'user_view.html',{'data':data})

def addstock(request):
    form=stockform
    if request.method=='POST':
        form=stockform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_view')
    return render(request,'addstock.html',{'form':form})

def s_view(request):
    return render(request,'sview.html')


def stock_view(request):
    a = stock.objects.all()
    return render(request,'stock.html',{'a':a})

def userstk_view(request):
    a = stock.objects.all()
    return render(request,'userstk_view.html',{'a':a})

def delete_stock(request,id):
    d=stock.objects.get(id=id)
    if request.method=='POST':
        d.delete()
        return redirect("stock_view")
    else:
        return redirect("stock_view")




def update_stock(request,id):
    data=stock.objects.get(id=id)
    stk=stockform(instance=data)
    if request.method=='POST':
        stk=stockform(request.POST or None,instance=data)
        if stk.is_valid():
            stk.save()
            return redirect('stock_view')
    return render(request,'update.html',{'stk':stk})


