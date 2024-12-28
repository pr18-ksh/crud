from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Article,Author,Contact,Student,Stduents,Course 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    std = Student.objects.all()
    return render(request,"std/home.html",{'std': std})

@login_required(login_url="/crud/login/")
def std_add(request):
    if request.method=='POST':
      #retrieve the user inputs
      
      stds_roll=request.POST.get("std_roll")
      stds_name=request.POST.get("std_name")
      stds_email=request.POST.get("std_email")
      stds_address=request.POST.get("std_address") 
      stds_phone=request.POST.get("std_phone")
      
      #create an object for models 
      s =Student()
      s.roll=stds_roll
      s.name=stds_name
      s.email=stds_email
      s.address=stds_address
      s.phone=stds_phone
      
      s.save()
      return redirect("/crud/home")
 
    return render(request,"std/add_std.html",{})

@login_required(login_url="/crud/login/")
def delete_std(request,roll):
    
    s=Student.objects.get(pk=roll)
    s.delete()
    
    return redirect("/crud/home/")

@login_required(login_url="/crud/login/")
def update_std(request,roll):
    std=Student.objects.get(pk=roll)
    return render(request,"std/update_std.html",{'std':std})

@login_required(login_url="/crud/login/")
def do_update_std(request,roll):
    std_roll = request.POST.get("std_roll")
    std_name = request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_address=request.POST.get("std_address")
    std_phone=request.POST.get("std_phone")
    
    std=Student.objects.get(pk=roll)
    std.roll=std_roll
    std.name=std_name
    std.email=std_email
    std.address=std_address
    std.phone=std_phone
    
    std.save()
    return redirect("/crud/home/")

def index(request):
    # author = Author.objects.create(name="pratik")
    # author=Author.objects.get(id=1)
    # contact=Contact.objects.create(author=author,address="Testing address")
    
    # Article.objects.create(author=author,title="article1",content="pratik.k")
    # Article.objects.create(author=author,title="article2",content="pratik.k")
    # articles_by_author=author.articles.all()
    # articles_by_author[1].title
    # article = Article.objects.get(id=2)
    
    # Stduents.objects.create(name="Student 1")
    # Stduents.objects.create(name="Student 2")
    
    # Course.objects.create(title="javascript developer")
    # Course.objects.create(title="Python developer")
    
    # student1 = Stduents.objects.get(id=1)
    course1 = Course.objects.get(id=1)
    # course2 = Course.objects.get(id=2)
    
    
    # course1.students.add(student1)
    # course2.students.add(student1)
    # student1.courses.all()[1].title
    return HttpResponse(course1.students.all()[0].name)

def login_page(request):
    
    if request.method == "POST":
       username= request.POST.get('username')
       password= request.POST.get('password')
       
       if not User.objects.filter(username=username).exists():
           messages.error(request,"Invalid user Credentials")
           return redirect('/crud/login/')
        
       user = authenticate(username=username,password=password)
           
       if user is None:
          messages.error(request,"invalid password")
          return redirect('/crud/login/')
         
       else:
           login(request,user)
           return redirect('/crud/home/')
        
               
    return render(request,"std/login.html",{})

def logout_page(request):
    logout(request)
    return redirect('/crud/login/')
       
def register_page(request):
    
    if request.method == "POST":
       first_name= request.POST.get('Firstname')
       last_name= request.POST.get('Lastname')
       username= request.POST.get('username')
       password= request.POST.get('password')
       
       user = User.objects.filter(username=username)
       
       if user.exists():
           messages.info(request, "Username already taken.")
           return redirect("/crud/register/")
    
       user= User.objects.create(
               first_name=first_name,
               last_name=last_name,
               username=username,
                 )
       user.set_password(password)
       user.save()
       messages.info(request, "Account created successfully.") 
       return redirect("/crud/register/")
    return render(request,"std/register.html",{})