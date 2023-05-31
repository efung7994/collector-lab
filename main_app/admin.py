from django.contrib import admin
# import your models here
from .models import Croc, Feeding, Toy

# Register your models here
admin.site.register(Croc)
admin.site.register(Feeding)
admin.site.register(Toy)