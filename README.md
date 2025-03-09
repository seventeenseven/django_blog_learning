# django_blog_learning

## Description

**django_blog_learning** est un projet de blog développé avec Django, conçu spécifiquement pour des fins d'apprentissage. Ce projet permet de créer et d'afficher des articles dans un template élégant, tout en intégrant des fonctionnalités essentielles telles que l'authentification, l'enregistrement, la connexion et la gestion de profil.

Ce projet a été réalisé dans le but d'enseigner aux étudiants les concepts fondamentaux du développement web avec Django, tout en mettant en pratique leurs compétences en Python.

## Fonctionnalités

- Création et affichage d'articles
- Authentification des utilisateurs
- Inscription et connexion
- Gestion de profil utilisateur
- Interface utilisateur élégante et intuitive
- Intégration avec l'API NewsAPI pour récupérer des actualités

## Capture d'écran

Voici un aperçu de la page d'accueil de mon blog :

![Homepage Screenshot](blog_homepage.png) 

## Compétences

En tant qu'enseignant en Python et Django, ce projet sert de ressource pédagogique pour mes étudiants, leur permettant d'apprendre à travers un projet pratique et engageant.

## Installation

Pour installer et exécuter le projet localement, suivez les étapes ci-dessous :

1. Clonez le repository :
   ```bash
   git clone https://github.com/seventeenseven/django_blog_learning.git
   cd django_blog_learning
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Effectuez les migrations de base de données :
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

6. Accédez à l'application via `http://127.0.0.1:8000`.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des pull requests pour améliorer le projet.

