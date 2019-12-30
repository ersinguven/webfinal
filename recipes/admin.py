from django.contrib import admin
from .models import Recipe,ingredient,equipment

# Register your models here.
class IngredientInline(admin.TabularInline):
    model = ingredient
    extra = 3
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(ingredient)
admin.site.register(equipment)