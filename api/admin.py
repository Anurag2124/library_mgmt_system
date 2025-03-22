from django.contrib import admin
from .models import AdminUser, Book
# Register your models here.
admin.site.register(AdminUser)
admin.site.register(Book)