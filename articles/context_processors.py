# employes/context_processors.py

from .models import Categorie

def categories(request):
    all_categories = Categorie.objects.all()
    return {'categories': all_categories}
