from django.contrib import admin

# Register your models here.

from .models import TrioCompany ,MatrixSoft
list = [TrioCompany , MatrixSoft]

admin.site.register(list)





















