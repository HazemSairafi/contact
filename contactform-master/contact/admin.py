from django.contrib import admin
from .models import  *
# Register your models here.

admin.site.register(Post)
admin.site.register(WarningMessage)
admin.site.register(Ban)
admin.site.register(Banadmin)
