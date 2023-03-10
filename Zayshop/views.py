from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customers


def index(request):
    data = Customers.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)


def shop(request):
    return render(request, 'shop.html')
def login(request):
    data= Customers.objects.all()
    context = {"data":data}
    return render(request, 'login.html')


def contact(request):
    data = Customers.objects.all()
    context = {"data": data}
    return redirect(request, 'con')


# data input

def handlesignup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        myuser = User.objects.create_user(username, email)
        myuser.save()
        return render(request, "contact.html")


def insertData(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        query = Customers(name=name, email=email)
        query.save()
        return redirect("/")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')

        else:
            return redirect('/login')

    return render(request, "login.html")