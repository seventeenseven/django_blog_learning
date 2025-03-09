from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from articles.forms import ArticleForm, LoginForm
from .models import Article, Commentaire, Categorie, Actualites
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method == 'POST':
        #Dans la methode POST, on récupère les données du formulaire
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Utilisateur créé
            print(user.username, user.password)
            login(request, user)  #Utilisateur connecté à sa session
            print('After login', user)
            return redirect('home')
        return render(request, 'register.html', {"form": form})
    else :
        #Dans la méthode GET, on envoie le formulaire à remplir
        form = UserCreationForm() #3 champs : username, password1, password2
        return render(request, 'register.html', {"form": form})

@login_required
def logout_view(request):
    logout(request) #Détruire la session
    return redirect('login')

def home(request):
    mes_articles = Article.objects.all()[1:5]
    featured_article = Article.objects.get(id=1)
    actualites =  Actualites.objects.all()
    return render(request, 'home.html', {'articles':mes_articles, 
                                         'f_article': featured_article,
                                         'actualites': actualites[:5]})

@login_required
def list_posts(request):
    all_posts = Article.objects.all().order_by('-date_publication')[5:]
    return render(request, 'all_posts.html', {"posts": all_posts})

def category(request, nom):
    categorie =  Categorie.objects.get(nom=nom)
    articles_categorie = categorie.articles.all()
    return render(request, 'category.html', {'categorie': categorie,
                                            'articles': articles_categorie})

class ArticleListView(ListView):
    model = Article # select * from post
    template_name = 'all_posts.html'
    context_object_name = "posts" # clé à utiliser dans le template
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categorie.objects.all()  # Récupérer toutes les catégories
        context["recent_posts"] = Article.objects.order_by('-date_publication')[:5]  # Derniers articles
        return context
    
class ActualitesListView(ListView):
    model = Actualites # select * from post
    template_name = 'actualites.html'
    context_object_name = "posts" # clé à utiliser dans le template
    paginate_by = 6  #Nbre d'elements par page

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categorie.objects.all()  # Récupérer toutes les catégories
        context["recent_posts"] = Actualites.objects.order_by('-date_publication')[:5]  # Derniers articles
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')

    

'''
def postcreate(request):
    if request.method == "POST":
        #Recupere les données du formulaires
        my_form = ArticleForm(request.POST)
        print("IN POST")
        return redirect('posts')
    print(request.method)
    my_form = ArticleForm()
    return render(request, "post_create.html", {"form":my_form})
'''

def about(request):
    return render(request, 'about.html')

def post(request, id, type):
    #Requete pour identifier l'article spécifiquement
    #article = select * from article where id=id
    if type == 'article':
        post = Article.objects.get(id=id)
        commentaires = Commentaire.objects.filter(article_id=id)
        #post.commentaire_set.all()
    elif type == 'actualite':
        post = Actualites.objects.get(id=id)
        commentaires = None
    return render(request, 'post_detail.html', {'article': post,
                                                 'commentaires': commentaires})

'''
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post_detail.html'
    context_object_name = 'post'
'''

def post_comment(request, commentaire):
    #if request.method == "POST":

    return redirect(request, '/')

#GET, POST, PUT, DELETE, PATCH

class CommentaireCreateView(CreateView):
    model = Commentaire
    fields = ['nom', 'contenu']
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['id'] # Associer le commentaire à l'article
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail',kwargs={'id': self.kwargs['id']}) # Rediriger vers l'article après soumission

def add_comment(request, article_id):
    if request.method == 'POST':
        commentaire = request.POST['comment']  #request.POST[name_attribute]
        print(commentaire)
        article = Article.objects.get(id=article_id)
        Commentaire.objects.create(article=article,
                                   nom=commentaire[:10], 
                                   contenu= commentaire, 
                                   auteur=request.user)
        return redirect('post_detail', 'article', article_id)

"""def login(request):
    if request.method=="POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data['name']
            password= login_form.cleaned_data['password']
            print(name)
            return redirect('home')
    login_form = LoginForm()
    return render(request, 'login.html', {'form':login_form})
"""

def like(request):
    pass

def favoris(request):
    pass
