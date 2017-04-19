from django.contrib import admin

from .models import CharacterCrime, Character, Crimes

# Register your models here.
admin.site.register(Character)
admin.site.register(Crimes)
admin.site.register(CharacterCrime)