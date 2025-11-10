from django.contrib import admin
from perfumeapp.models import PerfumesDB,FragranceDB

# Register your models here.
admin.site.register(FragranceDB)
admin.site.register(PerfumesDB)
