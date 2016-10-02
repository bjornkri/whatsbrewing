from django.contrib import admin
from .models import Beer, Brew, Brewery


@admin.register(Brewery)
class BreweryAdmin(admin.ModelAdmin):
    pass


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    pass


@admin.register(Brew)
class BrewAdmin(admin.ModelAdmin):
    pass
