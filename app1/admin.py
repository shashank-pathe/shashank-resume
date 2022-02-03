from django.contrib import admin
from .models import Mail,Documents
# Register your models here.
@admin.register(Mail)
class CityAdmin(admin.ModelAdmin):
    list_display =['name','email','subject','message']
@admin.register(Documents)
class CityAdmin(admin.ModelAdmin):
    list_display =['cource','univercity','classs','subject','document']