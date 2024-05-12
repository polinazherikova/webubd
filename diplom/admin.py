from django.contrib import admin
from .models import Calculator,Question,QuickContact
# Register your models here.
admin.site.register(Calculator)
admin.site.register(Question)
admin.site.register(QuickContact)
