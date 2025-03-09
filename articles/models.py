from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    nom = models.CharField(max_length=100)

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField(null=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey('Categorie',related_name='articles', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'liked_articles', blank=True)
    favoris = models.ManyToManyField(User, related_name = 'favorite_articles', blank=True)
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True )
    
    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return "categorie " + self.nom 
    
#Table Commentaire
class Commentaire(models.Model):
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    nom= models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete = models.CASCADE)

class Actualites(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contenu = models.TextField(null=True)
    url = models.CharField(max_length=255)
    categorie = models.ForeignKey('Categorie',related_name='actualites', on_delete=models.DO_NOTHING, blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name = 'liked_actualites', blank=True)
    favoris = models.ManyToManyField(User, related_name = 'favorite_actualites', blank=True)
    image = models.CharField(max_length=500)
    
    def __str__(self):
        return self.titre