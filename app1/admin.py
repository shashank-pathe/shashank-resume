from django.contrib import admin
from .models import Mail
# Register your models here.
@admin.register(Mail)
class CityAdmin(admin.ModelAdmin):
    list_display =['name','email','subject','message']