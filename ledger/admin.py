from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine,]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)