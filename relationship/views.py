from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserProfile, Employee, Department, Project, Membership
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# 1. One-to-One Relationship (UserProfile and User)

def create_user_profile(request):
    user = User.objects.create_user(username='john', password='password123', email='john@example.com')
    profile = UserProfile.objects.create(user=user, bio='This is John\'s bio')
    return HttpResponse(f"User profile for {user.username} created with bio: {profile.bio}")

def get_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.userprofile  # Access the One-to-One relationship
    return HttpResponse(f"User: {user.username}, Bio: {profile.bio}")

# 2. Many-to-One Relationship (Employee and Department)

def create_employee(request):
    department = Department.objects.create(name='HR Department')
    employee = Employee.objects.create(name='Alice', department=department, designation='HR Manager')
    return HttpResponse(f"Employee {employee.name} created in {department.name}")

def get_department_employees(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    employees = department.employee_set.all()  # Access related employees via ForeignKey
    employee_names = ', '.join([employee.name for employee in employees])
    return HttpResponse(f"Employees in {department.name}: {employee_names}")

# 3. Many-to-Many Relationship (Employee and Project) with Through Model (Membership)

def create_project(request):
    project = Project.objects.create(name='Project X', description='A new project.')
    return HttpResponse(f"Project {project.name} created.")

def assign_employee_to_project(request, employee_id, project_id):
    employee = get_object_or_404(Employee, id=employee_id)
    project = get_object_or_404(Project, id=project_id)
    membership = Membership.objects.create(employee=employee, project=project, date_joined='2024-01-01', role='Developer')
    return HttpResponse(f"Employee {employee.name} assigned to project {project.name} as {membership.role}")

def get_employee_projects(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    memberships = employee.membership_set.all()  # Access the through model Membership
    projects = ', '.join([membership.project.name for membership in memberships])
    return HttpResponse(f"Employee {employee.name} is working on projects: {projects}")

def get_project_employees(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    memberships = project.membership_set.all()  # Access the through model Membership
    employees = ', '.join([membership.employee.name for membership in memberships])
    return HttpResponse(f"Project {project.name} has employees: {employees}")


