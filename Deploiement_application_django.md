### **Déploiement d’une application Django sur Heroku et AWS avec PostgreSQL**  

Nous allons suivre **des étapes détaillées** pour **déployer** l’application Django sur **Heroku**, en utilisant **PostgreSQL** en local et en production.  

## Pré-requis

- Avoir python, Django et un environnement virtuel installé pour votre application Django
- Avoir un compte Heroku et AWS

## Configurations

- Dans le fichier settings.py
* DEBUG = False
* STATIC_URL = '/static/'
* STATIC_ROOT = os.path.join(BASE_DIR, "static")

Ensuite lancez la commande :
```bash
python manage.py collectstatic
```
(load static...)
- Rajoutez les configs de sécurité :
 SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
<br>
## Fichiers essentiels pour Heroku :

1. Procfile 
2. requirements.txt : pip freeze > requirements.txt
3. runtime.txt
<br> <br>
## **📌 Étape 1 : Préparer le projet Django pour PostgreSQL**  

### **1. Installer PostgreSQL en local**  
Si ce n’est pas encore fait, installe **PostgreSQL** et **pgAdmin** :  
- **Windows** : https://www.postgresql.org/download/windows/
- **Mac** : `brew install postgresql`  
- **Linux (Ubuntu)** :  
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

Vérifier que PostgreSQL fonctionne :  
```bash
psql --version
```

### **2. Installer les dépendances nécessaires**  
Ajoute ces paquets à ton environnement virtuel :  
```bash
pip install psycopg2-binary dj-database-url gunicorn
```
- **psycopg2-binary** : Connecte Django à PostgreSQL.  
- **dj-database-url** : Permet de gérer la base de données via des URLs d’environnement.  
- **gunicorn** : Serveur WSGI pour exécuter Django sur Heroku.  

### **3. Configurer PostgreSQL en local**  
1. **Créer une base de données PostgreSQL locale**  
   - Ouvre PostgreSQL (avec `psql` ou pgAdmin).  
   - Exécute :  
     ```sql
     CREATE DATABASE mydb;
     CREATE USER myuser WITH PASSWORD 'mypassword';
     ALTER ROLE myuser SET client_encoding TO 'utf8';
     ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
     ALTER ROLE myuser SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
     ```

2. **Modifier `settings.py` pour utiliser PostgreSQL en local**  
   Trouve la section `DATABASES` et remplace :  
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydb',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Appliquer les migrations**  
   ```bash
   python manage.py migrate
   ```

---

## **📌 Étape 2 : Préparer le projet pour Heroku**  

### **1. Installer l’interface Heroku**  
Télécharge et installe [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) puis connecte-toi avec la commande :  
```bash
heroku login
```

### **2. Créer un fichier `Procfile` (important pour Heroku)**  
Dans le **dossier du projet**, crée un fichier `Procfile` :  
`
Ajoutes y :  
```text
web: gunicorn myproject.wsgi --log-file -
```
**Remplace `myproject`** par le nom réel de ton projet.

### **3. Ajouter un fichier `.env` (pour la configuration locale avec dotenv)**  
Crée un fichier `.env` à la racine du projet :  
```text
DATABASE_URL=postgres://myuser:mypassword@localhost:5432/mydb
DEBUG=True
```
Ensuite, installe **django-environ** et configure Django pour lire `.env` :  
```bash
pip install django-environ
```
Modifie `settings.py` :  
```python
import environ
import os

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': env.db(),
}
```

---

## **📌 Étape 3 : Déployer sur Heroku**  

### **1. Assure toi d'avoir tout envoyer sur git **

### **2. Créer une application sur Heroku**  
```bash
heroku create mydjangoapp (you must add payment information into your heroku account)
```
Remplace `mydjangoapp` par un nom unique.

### **3. Ajouter PostgreSQL sur Heroku**  
```bash
heroku addons:create heroku-postgresql:hobby-dev
```
Cela crée une base de données PostgreSQL **gratuite** sur Heroku.

### **4. Configurer les variables d’environnement**  
```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='.herokuapp.com'
```

### **5. Pousser le projet sur Heroku**  
Ajoute et commit les fichiers :  
```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

### **6. Appliquer les migrations en production**  
```bash
heroku run python manage.py migrate
```

### **7. Créer un superutilisateur (si besoin)**  
```bash
heroku run python manage.py createsuperuser
```

### **8. Lancer l’application sur Heroku**  
```bash
heroku open
```

---

## **📌 Étape 4 : Utiliser PostgreSQL en local et en production**  
- **Local** : La connexion se fait via **settings.py** avec `DATABASE_URL=postgres://myuser:mypassword@localhost:5432/mydb`  
- **Production** : Heroku gère automatiquement l’URL de la base PostgreSQL avec la commande :  
  ```bash
  heroku config
  ```
  Puis, dans `settings.py` :  
  ```python
  DATABASES = {
      'default': dj_database_url.config(conn_max_age=600)
  }
  ```

---

## **📌 Étape 5 : Automatiser le déploiement avec GitHub (optionnel)**  
Si tu veux que chaque **push sur GitHub** déclenche un déploiement :  
```bash
heroku git:remote -a mydjangoapp
git push heroku main
```
Ou configure **GitHub Actions** pour un déploiement **CI/CD**.
