from django.contrib import admin
from .models import Staff, Principal, Role

# Register your models here.
admin.site.register(Principal)
admin.site.register(Staff)
admin.site.register(Role)