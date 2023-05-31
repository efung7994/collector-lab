from django.contrib import admin
# import your models here
from .models import Croc, Feeding

# Register your models here
admin.site.register(Croc)
admin.site.register(Feeding)