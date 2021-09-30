from django.contrib import admin
from .models import  Beat,Contact,ArijitAddress

# Register your models here.
admin.site.register(Beat)
admin.site.register(Contact)
admin.site.register(ArijitAddress)
admin.site.site_title = "Root Arijit"
admin.site.site_header = "Beats Of Arijit"
admin.site.index_title = "Arijit"
