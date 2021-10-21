from django.contrib import admin
from .models import Test, Negocio, Contacto, Categ
# Register your models here.




admin.site.register(Categ)
admin.site.register(Negocio)
admin.site.register(Contacto)
admin.site.register(Test)
