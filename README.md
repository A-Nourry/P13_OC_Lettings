## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement a pour but de mettre l'application en production sur la plateforme Heroku à l'aide de Docker et CircleCI.

Dès lors que des modifications seront apportées à la branche main sur Github, le pipeline CircleCI déclenchera le déploiement en trois étapes : 

- La première étape consiste à créer l'application via les fichiers du dépôt github, puis de passer les différents tests du code. Si les tests échouent, l'étape suivante ne sera pas déclenchée. 
- Ensuite, la deuxième étape va créer une image docker puis la pousser sur le dépôt docker distant (DockerHub). 
- Enfin, la troisième étape, va permettre de conteneuriser l'application à l'aide de l'image de votre DockerHub, puis la déployer sur Heroku.

Chaque étapes aura besoin que la précédente passe pour déclencher la suivante, si ces trois étapes passent, votre application sera correctement déployée.

### Prérequis

- Un compte [CircleCI](https://circleci.com/signup/)
- Un compte [DockerHub](https://hub.docker.com/)
- Un compte et une application créé sur [Heroku](https://id.heroku.com/login) 

### CircleCI
Tout d'abord assurez-vous que vous avez lié CircleCI à votre Github. Ensuite, ajoutez votre projet github à votre dashboard CircleCI. Vous n'avez pas besoin que CircleCI vous génère un fichier `config.yml`, car il est déjà présent dans le dossier `.circleci` de l'application.

Le fichier `config.yml` est utilisé pour définir les étapes et les configurations pour CircleCI lors de la construction, du déploiement et des tests du projet.

Maintenant, vous aurez besoin de déclarer les variables d'environnement suivantes, dans l'interface web de CircleCI, Project Settings > Environment Variables : 
- DOCKER_PASSWORD : Mot de passe de votre compte DockerHub

- DOCKER_USERNAME : Identifiant de votre compte DockerHub

- HEROKU_API_KEY : Clé d'API de votre compte Heroku

- HEROKU_APP_NAME : Nom de vottre application Heroku

- SECRET_KEY : Clé secrète de l'application Django

### Docker

Les instructions pour la création de l'image docker se trouvent dans le fichier `Dockerfile` de l'application. La création et le déploiement sur votre compte se feront automatiquement à l'aide du fichier `config.yml` de CircleCI.

Assurez-vous juste de bien renseigner vos informations d'identification dans les variables d'environnement de CircleCI. (DOCKER_PASSWORD et DOCKER_USERNAME)

### Heroku

Sur l'interface web d'Heroku, créer une nouvelle application via `New > Create new app`.

Il faudra utiliser la méthode `Container Registry` pour déployer l'application sur Heroku. Les étapes sont définies dans le fichier `config.yml`.

Téléchargez et installez la console [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) afin de récupérer la clé d'API via la commande ```heroku auth:token```

Sur CircleCI assurez vous de bien avoir déclarer les variables d'environnement HEROKU_API_KEY et HEROKU_APP_NAME.

## Surveillance via Sentry

Sentry permet de suivre les bugs et les erreurs en temps réel de l'application, de les enregistrer et de les classer.

### Prérequis
- Un compte [Sentry](https://sentry.io/auth/login/)

### Configuration

Après avoir créé un compte, créez un nouveau projet à l'aide de `Create Project`.

Sur la page de configuration de votre projet Sentry, récupérer votre DSN Sentry afin de le déclarer dans les variables d'environnement de CircleCI.

Pour tester Sentry, déclenchez un bug a l'aide de la vue `sentry-debug` disponible via l'url http://localhost:8000/sentry-debug ou via https://heroku-app-name.herokuapp.com/sentry-debug