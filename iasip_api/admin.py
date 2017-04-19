from django.contrib import admin

from .models import CharacterCrime, Character, Crime
# Register your models here.
admin.site.register(Character)
admin.site.register(Crime)
admin.site.register(CharacterCrime)
