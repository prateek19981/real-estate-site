from django.contrib import admin
from realtors.models import Realtor 

# Register your models here.
class RealtorList(admin.ModelAdmin):
	list_display=('id','name','photo','email','hire_date','is_mvp')
	list_display_links=('id','name')
	search_fields=('name','is_mvp','hire_date')






admin.site.register(Realtor,RealtorList)
