from django.contrib import admin
from .models import Option, Riddle, Kits

admin.site.register(Kits)
admin.site.register(Riddle)
admin.site.register(Option)
