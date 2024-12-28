from django.contrib import admin
from .models import UserProfile, Department, Employee, Project, Membership

admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Membership)



