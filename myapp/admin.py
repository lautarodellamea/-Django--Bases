from django.contrib import admin
from .models import Project, Task

# Register your models here.
# este archivo es para que django pueda añadir nuestros modelos al panel de administración.
admin.site.register(Project)
admin.site.register(Task)
