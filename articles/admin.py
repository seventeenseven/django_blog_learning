from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Commentaire)
admin.site.register(Tag)
admin.site.register(Actualites)