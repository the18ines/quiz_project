
<div align="center">

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![JSONB](https://img.shields.io/badge/JSONB-NoSQL-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Projet Architecture Hybride — Système de Quiz Intelligent (SQL + NoSQL)**

*Application Django exploitant PostgreSQL + JSONB pour une gestion flexible des questionnaires et des réponses*

</div>

---

## 📋 Table des matières

- [Aperçu du projet](#-aperçu-du-projet)
- [Objectifs](#-objectifs)
- [Architecture hybride](#-architecture-hybride)
- [Modélisation des données](#-modélisation-des-données)
- [Structure SQL](#-structure-sql)
- [Structure NoSQL (JSONB)](#-structure-nosql-jsonb)
- [Fonctionnement du scoring](#-fonctionnement-du-scoring)
- [Architecture applicative Django](#-architecture-applicative-django)
- [Installation et configuration](#-installation-et-configuration)
- [Technologies utilisées](#-technologies-utilisées)

---

## 🎯 Aperçu du projet

Ce projet implémente une **application de gestion de quiz dynamique** basée sur une **architecture hybride (SQL + NoSQL)**.

Le système permet :

- À plusieurs administrateurs de créer des catégories et des questions  
- De définir des réponses correctes dynamiques  
- Aux utilisateurs de répondre aux questionnaires  
- De calculer automatiquement un score par catégorie  

L’originalité repose sur l’utilisation combinée de :

- **SQL (PostgreSQL)** → données structurées  
- **JSONB (NoSQL)** → données flexibles (questions, réponses)  

---

## 🎯 Objectifs

### Objectif principal

Développer une application Django exploitant efficacement une **architecture hybride SQL + NoSQL**.

### Objectifs spécifiques

- Démontrer quand utiliser SQL vs JSONB  
- Permettre une structure de quiz dynamique  
- Optimiser les performances de comparaison de réponses  
- Implémenter un système de scoring automatisé  
- Supporter plusieurs administrateurs (multi-superuser)  

---

## 🏗 Architecture hybride

┌──────────────────────┐
│ Application │
│ Django │
└──────────┬───────────┘
│
▼
┌──────────────────────────────┐
│ PostgreSQL DB │
│ │
│ SQL Tables │
│ - Utilisateurs │
│ - Catégories │
│ │
│ JSONB (NoSQL) │
│ - Questions dynamiques │
│ - Réponses flexibles │
└──────────────────────────────┘


---

## 🧠 Modélisation des données

L’architecture repose sur une séparation claire :

### 🔹 Données SQL (structurées)
- Utilisateurs  
- Administrateurs  
- Catégories  
- Métadonnées  

### 🔹 Données NoSQL (flexibles)
- Contenu des questions  
- Réponses utilisateurs  
- Réponses correctes  
- Structure des quiz  

---

## 🗄 Structure SQL

### 👤 Table PERSONNE

| Champ | Type |
|------|-----|
| id_personne | PK |
| nom | string |
| prenom | string |
| email | string |
| mdp | string |
| date_inscription | datetime |
| est_actif | boolean |

---

### 👤 Table UTILISATEUR

| Champ | Type |
|------|-----|
| id_personne | PK, FK |
| pseudo | string |
| score_total | integer |
| nombre_question_repondu | integer |

---

### 👑 Table ADMINISTRATEUR

| Champ | Type |
|------|-----|
| id_personne | PK, FK |
| est_superadmin | boolean |

---

### 📂 Table CATEGORIE

| Champ | Type |
|------|-----|
| id_categorie | PK |
| libelle | string |
| date_creation | datetime |

---

## 🧩 Structure NoSQL (JSONB)

### ❓ Table QUESTION

| Champ | Type |
|------|-----|
| id_question | PK |
| id_categorie | FK |
| id_personne | FK |
| contenu | JSONB |
| date_creation | datetime |


---

## 🧠 Modélisation des données

L’architecture repose sur une séparation claire :

### 🔹 Données SQL (structurées)
- Utilisateurs  
- Administrateurs  
- Catégories  
- Métadonnées  

### 🔹 Données NoSQL (flexibles)
- Contenu des questions  
- Réponses utilisateurs  
- Réponses correctes  
- Structure des quiz  

---

## 🗄 Structure SQL

### 👤 Table PERSONNE

| Champ | Type |
|------|-----|
| id_personne | PK |
| nom | string |
| prenom | string |
| email | string |
| mdp | string |
| date_inscription | datetime |
| est_actif | boolean |

---

### 👤 Table UTILISATEUR

| Champ | Type |
|------|-----|
| id_personne | PK, FK |
| pseudo | string |
| score_total | integer |
| nombre_question_repondu | integer |

---

### 👑 Table ADMINISTRATEUR

| Champ | Type |
|------|-----|
| id_personne | PK, FK |
| est_superadmin | boolean |

---

### 📂 Table CATEGORIE

| Champ | Type |
|------|-----|
| id_categorie | PK |
| libelle | string |
| date_creation | datetime |

---

## 🧩 Structure NoSQL (JSONB)

### ❓ Table QUESTION

| Champ | Type |
|------|-----|
| id_question | PK |
| id_categorie | FK |
| id_personne | FK |
| contenu | JSONB |
| date_creation | datetime |
}

🧱 Architecture applicative Django
Applications
accounts → gestion utilisateurs/admin
quiz → catégories + questions
responses → réponses + scoring


🚀 Installation et configuration
django-admin startproject quiz_project
cd quiz_project

python manage.py startapp accounts
python manage.py startapp quiz
python manage.py startapp responses
Configuration PostgreSQL

Dans settings.py :

INSTALLED_APPS = [
    'django.contrib.postgres',
]
Migration
python manage.py makemigrations
python manage.py migrate
Création superuser
python manage.py createsuperuser

✔️ Plusieurs administrateurs possibles

🧰 Technologies utilisées
Backend : Django (Python)
Base de données : PostgreSQL
NoSQL intégré : JSONB
ORM : Django ORM
Langage : Python

👨‍💻 Auteur
Marissa DJOMO
Projet académique — Architecture des systèmes hybrides


⭐ Conclusion

Ce projet démontre concrètement comment exploiter une architecture hybride SQL + NoSQL dans une application réelle, en combinant rigidité structurelle et flexibilité dynamique.
