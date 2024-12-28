from django.urls import path
from .views import *
urlpatterns = [
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
    path('get_user_profile/<int:user_id>/', get_user_profile, name='get_user_profile'),
    path('create_employee/', create_employee, name='create_employee'),
    path('get_department_employees/<int:department_id>/', get_department_employees, name='get_department_employees'),
    path('create_project/', create_project, name='create_project'),
    path('assign_employee_to_project/<int:employee_id>/<int:project_id>/', assign_employee_to_project, name='assign_employee_to_project'),
    path('get_employee_projects/<int:employee_id>/', get_employee_projects, name='get_employee_projects'),
    path('get_project_employees/<int:project_id>/', get_project_employees, name='get_project_employees'),
   
]
