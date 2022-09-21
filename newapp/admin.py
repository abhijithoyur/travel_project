from django.contrib import admin

from .models import Place
from .models import Persons
admin.site.register(Place)
admin.site.register(Persons)
