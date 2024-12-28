from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
class Student(models.Model):
    roll = models.CharField(max_length=100)
    name= models.CharField(max_length=50,db_index=True)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    is_deleted=models.BooleanField(default=False)
    
    objects = StudentManager()
    admin_objects=models.Manager()
    
class Car(models.Model):
   car_name=models.CharField(max_length=100)
   speed=models.IntegerField(default=20)

   def __str__(self):
       return self.car_name

#one to one relationship
class Author(models.Model):
    name=models.CharField(max_length=200)
    
class Contact(models.Model):
    address=models.CharField(max_length=150)
    author=models.OneToOneField(Author,on_delete=models.CASCADE)

#many to one relationship  
class Question(models.Model):
    text = models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')
    
    def __str___(self):
        return self.text

class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_txt=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

#one to many relationship
class Article(models.Model):
    title=models.CharField(max_length=2000)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='articles')

#manytomany relationship models

class Course(models.Model):
    title=models.CharField(max_length=2000)

class Stduents(models.Model):
      user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
      name=models.CharField(max_length=2000)
      courses=models.ManyToManyField('Course',related_name='students')



      
      

    