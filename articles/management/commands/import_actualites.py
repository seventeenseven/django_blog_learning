import requests
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from articles.models import Actualites, Categorie


class Command(BaseCommand):
    help = "Importer des actualités d'une categorie a partir de News API \
        python manage.py import_actualites <nom_de _la_categorie>"

    def add_arguments(self, parser):
        parser.add_argument("categorie", nargs="+", type=str)

    def handle(self, *args, **kwargs):
        categorie=kwargs["categorie"][0]
        print(categorie)
        API_KEY = 'd39af74949244c76a8eb4cae5aafffdc'
        api_url = f'https://newsapi.org/v2/top-headlines?country=us&category={categorie}&apiKey={API_KEY}'

        response = requests.get(api_url)
        data = response.json()
        
        print('Statut : ',data['status'])
        print('Nombre de resultats : ',data['totalResults'])
        #print('Les deux premiers articles : ')
        #print(data['articles'][0])

        added = 0
        category = Categorie.objects.get(nom=categorie.title())
        for article in data.get('articles', []):
            titre = article['title'] or ''
            description = article['description'] or ''
            contenu = article['content'] or ''
            url = article['url'] or ''
            date_publication = parse_datetime(article['publishedAt']) or ''
            auteur = article['author'] or ''
            image = article['urlToImage'] or ''

            if not Actualites.objects.filter(titre=titre).exists():
                Actualites.objects.create(
                    titre = titre,
                    description = description,
                    contenu = contenu,
                    url = url,
                    date_publication = date_publication,
                    auteur = auteur,
                    image = image,
                    categorie = category
                )
                added+=1
        self.stdout.write(
                self.style.SUCCESS(f' {added} Actualités importés !'))

