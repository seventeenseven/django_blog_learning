from django.urls import path
#from .views import CommentaireCreateView, home, list_posts, about, \
#    post, post_comment, ArticleListView, ArticleCreateView, LoginView
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    #path('posts/', list_posts, name='posts'),
    path('posts/', ArticleListView.as_view(), name='posts'),
    path('news/', ActualitesListView.as_view(), name='news'),
    path('create_post/', ArticleCreateView.as_view(), name='create_post'),
    path('about/', about, name='about'),
    path('post/<str:type>/<int:id>', post, name='post_detail'),
    path('category/<str:nom>', category, name="category"),
    path('posts/comment/', CommentaireCreateView.as_view(), name='comment_create'),
    path('like/', like, name='like'),

    #Authentification
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

    #Commentaires
    path('add_comment/<int:article_id>', add_comment, name='add_comment')
]


