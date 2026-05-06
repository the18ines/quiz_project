import os
import django
import json
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from accounts.models import Personne
from quiz.models import Categorie, Question
from responses.models import Reponse, Score

# Créer un utilisateur admin s'il n'existe pas
admin_user, created = Personne.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin3@quiz.com',
        'is_staff': True,
        'is_superuser': True
    }
)
if created:
    admin_user.set_password('admin3456789')
    admin_user.save()
    print("Utilisateur admin créé")

# Catégories avec leurs structures JSONB
categories_data = [
    {
        "libelle": "NoSQL",
        "structure_questions": {
            "description": "Quiz sur les bases de données NoSQL",
            "difficulte": "intermédiaire",
            "duree_minutes": 15,
            "nombre_questions": 5,
            "tags": ["bdd", "nosql", "mongodb", "cassandra"]
        }
    },
    {
        "libelle": "Python",
        "structure_questions": {
            "description": "Quiz sur le langage Python",
            "difficulte": "facile",
            "duree_minutes": 10,
            "nombre_questions": 5,
            "tags": ["python", "programmation", "langage"]
        }
    },
    {
        "libelle": "JSON",
        "structure_questions": {
            "description": "Quiz sur JSON et JSONB",
            "difficulte": "débutant",
            "duree_minutes": 10,
            "nombre_questions": 5,
            "tags": ["json", "jsonb", "data"]
        }
    },
    {
        "libelle": "PostgreSQL",
        "structure_questions": {
            "description": "Quiz sur PostgreSQL et JSONB",
            "difficulte": "intermédiaire",
            "duree_minutes": 15,
            "nombre_questions": 5,
            "tags": ["postgresql", "sql", "bdd"]
        }
    },
    {
        "libelle": "MongoDB",
        "structure_questions": {
            "description": "Quiz sur MongoDB",
            "difficulte": "intermédiaire",
            "duree_minutes": 15,
            "nombre_questions": 5,
            "tags": ["mongodb", "nosql", "document"]
        }
    },
    {
        "libelle": "Django",
        "structure_questions": {
            "description": "Quiz sur le framework Django",
            "difficulte": "intermédiaire",
            "duree_minutes": 20,
            "nombre_questions": 6,
            "tags": ["django", "python", "web"]
        }
    },
    {
        "libelle": "API REST",
        "structure_questions": {
            "description": "Quiz sur les API REST",
            "difficulte": "intermédiaire",
            "duree_minutes": 15,
            "nombre_questions": 5,
            "tags": ["api", "rest", "http"]
        }
    },
    {
        "libelle": "SQL vs NoSQL",
        "structure_questions": {
            "description": "Comparaison entre SQL et NoSQL",
            "difficulte": "avancé",
            "duree_minutes": 20,
            "nombre_questions": 6,
            "tags": ["sql", "nosql", "comparaison"]
        }
    },
    {
        "libelle": "Cassandra",
        "structure_questions": {
            "description": "Quiz sur Apache Cassandra",
            "difficulte": "avancé",
            "duree_minutes": 20,
            "nombre_questions": 6,
            "tags": ["cassandra", "nosql", "distribué"]
        }
    },
    {
        "libelle": "Redis",
        "structure_questions": {
            "description": "Quiz sur Redis",
            "difficulte": "intermédiaire",
            "duree_minutes": 15,
            "nombre_questions": 5,
            "tags": ["redis", "cache", "nosql"]
        }
    }
]

# Questions pour chaque catégorie
questions_data = {
    "NoSQL": [
        {
            "contenu": {
                "texte": "Que signifie l'acronyme NoSQL ?",
                "type": "qcm",
                "options": ["Not Only SQL", "No SQL", "Non-Standard Query Language", "New SQL"],
                "reponse_correcte": "Not Only SQL"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Parmi ces bases de données, laquelle est une base NoSQL ?",
                "type": "qcm",
                "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"],
                "reponse_correcte": "MongoDB"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel type de base NoSQL utilise MongoDB ?",
                "type": "qcm",
                "options": ["Clé-valeur", "Colonnes", "Graphes", "Documents"],
                "reponse_correcte": "Documents"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Lequel de ces avantages est propre aux bases NoSQL ?",
                "type": "qcm",
                "options": ["Scalabilité horizontale", "Intégrité référentielle", "Transactions ACID", "Schéma strict"],
                "reponse_correcte": "Scalabilité horizontale"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel est l'inconvénient majeur des bases NoSQL ?",
                "type": "question_libre",
                "reponse_correcte": "Manque de standardisation et de transactions ACID complètes"
            },
            "points": 15
        }
    ],
    
    "Python": [
        {
            "contenu": {
                "texte": "Quelle est la sortie de: print(type(10)) ?",
                "type": "qcm",
                "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'list'>"],
                "reponse_correcte": "<class 'int'>"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Comment crée-t-on une liste en Python ?",
                "type": "qcm",
                "options": ["{}", "()", "[]", "<>"],
                "reponse_correcte": "[]"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quelle est la sortie de: 'Hello' + ' ' + 'World' ?",
                "type": "qcm",
                "options": ["Hello World", "Hello+World", "HelloWorld", "Erreur"],
                "reponse_correcte": "Hello World"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel mot-clé utilise-t-on pour définir une fonction ?",
                "type": "qcm",
                "options": ["function", "def", "func", "define"],
                "reponse_correcte": "def"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Python est un langage... ?",
                "type": "qcm",
                "options": ["Compilé", "Interprété", "Assembleur", "Machine"],
                "reponse_correcte": "Interprété"
            },
            "points": 10
        }
    ],
    
    "JSON": [
        {
            "contenu": {
                "texte": "Que signifie JSON ?",
                "type": "qcm",
                "options": ["JavaScript Object Notation", "Java Standard Object Notation", "JavaScript Online Notation", "JSON Object Notation"],
                "reponse_correcte": "JavaScript Object Notation"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel type de données utilise JSON ?",
                "type": "qcm",
                "options": ["Texte", "Binaire", "XML", "CSV"],
                "reponse_correcte": "Texte"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Que signifie JSONB dans PostgreSQL ?",
                "type": "qcm",
                "options": ["JSON Binary", "JSON Byte", "JSON Basic", "JSON Backup"],
                "reponse_correcte": "JSON Binary"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel est l'avantage de JSONB par rapport à JSON ?",
                "type": "qcm",
                "options": ["Performance", "Lisibilité", "Compression", "Tous ces avantages"],
                "reponse_correcte": "Tous ces avantages"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Donnez un exemple de structure JSON valide",
                "type": "question_libre",
                "reponse_correcte": '{"nom": "Jean", "age": 30}'
            },
            "points": 15
        }
    ],
    
    "PostgreSQL": [
        {
            "contenu": {
                "texte": "Quel type de données PostgreSQL permet de stocker du JSON indexé ?",
                "type": "qcm",
                "options": ["JSON", "JSONB", "TEXT", "XML"],
                "reponse_correcte": "JSONB"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel opérateur utilise-t-on pour accéder à un champ JSONB ?",
                "type": "qcm",
                "options": ["->", ".", "/", "=>"],
                "reponse_correcte": "->"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Comment indexer un champ JSONB en PostgreSQL ?",
                "type": "qcm",
                "options": ["GIN", "BTREE", "HASH", "BRIN"],
                "reponse_correcte": "GIN"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quelle fonction PostgreSQL vérifie l'existence d'une clé JSONB ?",
                "type": "qcm",
                "options": ["jsonb_exists", "? (opérateur)", "has_key", "contains"],
                "reponse_correcte": "? (opérateur)"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Citez un avantage de JSONB par rapport au JSON standard",
                "type": "question_libre",
                "reponse_correcte": "Indexation et meilleures performances"
            },
            "points": 15
        }
    ],
    
    "MongoDB": [
        {
            "contenu": {
                "texte": "Comment appelle-t-on une 'ligne' dans MongoDB ?",
                "type": "qcm",
                "options": ["Document", "Enregistrement", "Ligne", "Tuple"],
                "reponse_correcte": "Document"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel langage utilise MongoDB pour les requêtes ?",
                "type": "qcm",
                "options": ["SQL", "JSON", "JavaScript", "Python"],
                "reponse_correcte": "JSON"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Que signifie BSON ?",
                "type": "qcm",
                "options": ["Binary JSON", "Basic JSON", "Byte JSON", "Big JSON"],
                "reponse_correcte": "Binary JSON"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quelle commande MongoDB permet de créer une base de données ?",
                "type": "qcm",
                "options": ["CREATE DATABASE", "use nomBD", "new database", "make db"],
                "reponse_correcte": "use nomBD"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "MongoDB utilise-t-il des schémas stricts ?",
                "type": "question_libre",
                "reponse_correcte": "Non, MongoDB est sans schéma"
            },
            "points": 15
        }
    ],
    
    "Django": [
        {
            "contenu": {
                "texte": "Quelle commande crée un nouveau projet Django ?",
                "type": "qcm",
                "options": ["django startproject", "django-admin startproject", "python manage.py startproject", "django create project"],
                "reponse_correcte": "django-admin startproject"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Que signifie MVT dans Django ?",
                "type": "qcm",
                "options": ["Model-View-Template", "Model-View-Controller", "Module-View-Template", "Model-Validation-Template"],
                "reponse_correcte": "Model-View-Template"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel fichier contient les URLs d'un projet Django ?",
                "type": "qcm",
                "options": ["views.py", "models.py", "urls.py", "settings.py"],
                "reponse_correcte": "urls.py"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Comment applique-t-on les migrations dans Django ?",
                "type": "qcm",
                "options": ["python manage.py migrate", "python manage.py makemigrations", "django migrate", "python migrate"],
                "reponse_correcte": "python manage.py migrate"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel ORM utilise Django par défaut ?",
                "type": "question_libre",
                "reponse_correcte": "Django ORM"
            },
            "points": 15
        },
        {
            "contenu": {
                "texte": "Dans quel fichier définit-on les modèles Django ?",
                "type": "qcm",
                "options": ["views.py", "models.py", "admin.py", "forms.py"],
                "reponse_correcte": "models.py"
            },
            "points": 10
        }
    ],
    
    "API REST": [
        {
            "contenu": {
                "texte": "Que signifie REST ?",
                "type": "qcm",
                "options": ["Representational State Transfer", "Rapid Easy Simple Transfer", "Request State Transfer", "Representational Simple Transfer"],
                "reponse_correcte": "Representational State Transfer"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quelle méthode HTTP est utilisée pour lire des données ?",
                "type": "qcm",
                "options": ["POST", "PUT", "GET", "DELETE"],
                "reponse_correcte": "GET"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel code HTTP indique une création réussie ?",
                "type": "qcm",
                "options": ["200", "201", "204", "404"],
                "reponse_correcte": "201"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel format de données est le plus utilisé pour les API REST ?",
                "type": "qcm",
                "options": ["XML", "JSON", "CSV", "YAML"],
                "reponse_correcte": "JSON"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quelle méthode HTTP est idempotente ?",
                "type": "question_libre",
                "reponse_correcte": "GET, PUT, DELETE"
            },
            "points": 15
        }
    ],
    
    "SQL vs NoSQL": [
        {
            "contenu": {
                "texte": "Quel type de base de données utilise un schéma fixe ?",
                "type": "qcm",
                "options": ["SQL", "NoSQL", "Les deux", "Aucune"],
                "reponse_correcte": "SQL"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Laquelle supporte mieux la scalabilité horizontale ?",
                "type": "qcm",
                "options": ["SQL", "NoSQL", "Les deux également", "Aucune"],
                "reponse_correcte": "NoSQL"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel type garantit mieux l'ACID ?",
                "type": "qcm",
                "options": ["SQL", "NoSQL", "Les deux", "Aucune"],
                "reponse_correcte": "SQL"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Lequel est mieux adapté pour des données non structurées ?",
                "type": "qcm",
                "options": ["SQL", "NoSQL", "Les deux", "Aucune"],
                "reponse_correcte": "NoSQL"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Citez une base de données SQL et une NoSQL",
                "type": "question_libre",
                "reponse_correcte": "PostgreSQL (SQL) et MongoDB (NoSQL)"
            },
            "points": 15
        },
        {
            "contenu": {
                "texte": "Quel langage utilise-t-on pour SQL ?",
                "type": "qcm",
                "options": ["SQL", "JSON", "Python", "Java"],
                "reponse_correcte": "SQL"
            },
            "points": 10
        }
    ],
    
    "Cassandra": [
        {
            "contenu": {
                "texte": "Quel type de base NoSQL est Cassandra ?",
                "type": "qcm",
                "options": ["Colonnes", "Documents", "Clé-valeur", "Graphes"],
                "reponse_correcte": "Colonnes"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Cassandra a été développé par quelle entreprise ?",
                "type": "qcm",
                "options": ["Facebook", "Google", "Amazon", "Microsoft"],
                "reponse_correcte": "Facebook"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quel langage de requête utilise Cassandra ?",
                "type": "qcm",
                "options": ["CQL", "SQL", "NoSQL", "JSON"],
                "reponse_correcte": "CQL"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Cassandra est-elle une base AP ou CP ?",
                "type": "qcm",
                "options": ["AP (Available + Partition tolerant)", "CP (Consistent + Partition tolerant)", "CA", "ACID"],
                "reponse_correcte": "AP (Available + Partition tolerant)"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Cassandra supporte-t-elle les transactions ?",
                "type": "question_libre",
                "reponse_correcte": "Non, Cassandra ne supporte pas les transactions ACID complètes"
            },
            "points": 15
        },
        {
            "contenu": {
                "texte": "Quel protocole utilise Cassandra pour la réplication ?",
                "type": "qcm",
                "options": ["Gossip", "Raft", "Paxos", "Zab"],
                "reponse_correcte": "Gossip"
            },
            "points": 10
        }
    ],
    
    "Redis": [
        {
            "contenu": {
                "texte": "Quel type de base NoSQL est Redis ?",
                "type": "qcm",
                "options": ["Clé-valeur", "Documents", "Colonnes", "Graphes"],
                "reponse_correcte": "Clé-valeur"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Redis stocke les données principalement dans... ?",
                "type": "qcm",
                "options": ["Mémoire RAM", "Disque dur", "SSD", "Cloud"],
                "reponse_correcte": "Mémoire RAM"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Redis est souvent utilisé comme... ?",
                "type": "qcm",
                "options": ["Cache", "Base de données principale", "File d'attente", "Tous ces usages"],
                "reponse_correcte": "Tous ces usages"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Quelle commande Redis récupère une valeur ?",
                "type": "qcm",
                "options": ["GET", "SET", "RETRIEVE", "FETCH"],
                "reponse_correcte": "GET"
            },
            "points": 10
        },
        {
            "contenu": {
                "texte": "Redis supporte-t-il la persistance des données ?",
                "type": "question_libre",
                "reponse_correcte": "Oui, Redis supporte la persistance via RDB ou AOF"
            },
            "points": 15
        }
    ]
}

# Insertion des données
print("\nCréation des catégories et questions...\n")

for cat_data in categories_data:
    # Créer la catégorie
    categorie, created = Categorie.objects.get_or_create(
        libelle=cat_data["libelle"],
        defaults={
            'structure_questions': cat_data["structure_questions"],
            'createur': admin_user
        }
    )
    
    if created:
        print(f"Catégorie créée: {categorie.libelle}")
        
        # Ajouter les questions pour cette catégorie
        if cat_data["libelle"] in questions_data:
            for q_data in questions_data[cat_data["libelle"]]:
                question = Question.objects.create(
                    categorie=categorie,
                    contenu=q_data["contenu"],
                    points=q_data["points"],
                    createur=admin_user
                )
                print(f"  Question ajoutée: {q_data['contenu']['texte'][:50]}...")
    else:
        print(f"Catégorie existe déjà: {categorie.libelle}")

print("\nGénération des données terminée !")
print(f"\nRésumé:")
print(f"   - {Categorie.objects.count()} catégories")
print(f"   - {Question.objects.count()} questions")
print(f"\Pour vous connecter:")
print(f"   Username: admin3")
print(f"   Password: admin3456789")