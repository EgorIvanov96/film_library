from django.contrib import admin

from .models import Movies, Favorites


admin.site.register(Movies)
admin.site.register(Favorites)
admin.site.empty_value_display = 'не задано'
