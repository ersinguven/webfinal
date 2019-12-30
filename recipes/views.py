from django.shortcuts import render
from django.views import generic
from .models import Recipe,ingredient,equipment
from django.views.generic import CreateView
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        return Recipe.objects.all()

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ('name','cuisine','difficulty','pub_date','image','rating','price','instructions','video')
    success_url = "/recipes"