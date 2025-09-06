# Custom Theme Color Odoo

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## 🎨 Description

**Custom Theme Color Odoo** est un module qui permet de personnaliser facilement les couleurs de l'interface Odoo en remplaçant la couleur violette par défaut (`#875A7B`) par vos couleurs d'entreprise.

### ✨ Fonctionnalités

- ✅ Remplacement de la couleur principale d'Odoo
- ✅ Personnalisation des boutons, liens et éléments interactifs
- ✅ Modification des couleurs dans les emails automatiques
- ✅ Support des badges, tags et étiquettes
- ✅ Compatible interface backend et frontend
- ✅ Configuration centralisée via variables CSS
- ✅ Compatible mode sombre/clair

### 🎯 Zones couvertes

- Boutons principaux et secondaires
- Liens et éléments de navigation
- Pagination et contrôles
- Formulaires et champs de saisie
- Badges et indicateurs de statut
- Tags et étiquettes
- Templates d'emails
- Barres de progression et indicateurs

## 📁 Structure du module

```
custom_theme/
├── __init__.py
├── __manifest__.py
├── data/
│   └── color_config.xml
├── views/
│   └── email_templates.xml
└── static/
    └── src/
        └── css/
            ├── variables.css
            └── custom.css
```

## 🚀 Installation

### Méthode 1 : Installation depuis GitHub

1. **Clonez le repository dans votre dossier addons :**
   ```bash
   cd /chemin/vers/odoo/addons
   git clone https://github.com/Garconposey/custom-theme-color-odoo.git custom_theme
   ```

2. **Redémarrez votre serveur Odoo :**
   ```bash
   ./odoo-bin -u all -d votre_base_de_donnees
   ```

3. **Installez le module :**
   - Allez dans `Apps` > `Mettre à jour la liste des Apps`
   - Recherchez "Custom Theme Colors"
   - Cliquez sur `Installer`

### Méthode 2 : Installation manuelle

1. **Téléchargez le module et placez-le dans votre dossier addons**
2. **Redémarrez Odoo et installez le module via l'interface**

## ⚙️ Configuration

### 🎨 Personnaliser les couleurs

**Option 1 : Modification des variables CSS (Recommandée)**

Éditez le fichier `static/src/css/variables.css` :

```css
:root {
    --custom-primary: #2DBAE8;      /* Votre couleur principale */
    --custom-primary-dark: #024155; /* Version foncée pour les hover */
    --custom-primary-light: #2DBAE854; /* Version claire/transparente */
}
```

**Option 2 : Configuration via l'interface Odoo**

Les couleurs peuvent aussi être modifiées via les paramètres système :
- `custom_theme.color_primary`
- `custom_theme.color_primary_dark` 
- `custom_theme.color_primary_light`

### 🎨 Exemples de palettes de couleurs

```css
/* Bleu professionnel */
--custom-primary: #0066CC;
--custom-primary-dark: #004499;

/* Vert moderne */
--custom-primary: #2ECC40;
--custom-primary-dark: #1F8B2C;

/* Orange énergique */
--custom-primary: #FF6B35;
--custom-primary-dark: #E55A2B;

/* Rouge corporate */
--custom-primary: #DC3545;
--custom-primary-dark: #C82333;
```

### 🔧 Personnalisation avancée

Pour ajouter vos propres styles, éditez `static/src/css/custom.css` :

```css
/* Vos styles personnalisés */
.mon-element-custom {
    background-color: var(--custom-primary) !important;
    color: white !important;
}
```

## 🛠️ Développement

### Ajouter de nouveaux sélecteurs CSS

Si certains éléments violets ne sont pas couverts :

1. **Identifiez l'élément avec l'inspecteur (F12)**
2. **Ajoutez le sélecteur dans `custom.css` :**
   ```css
   .nouveau-selecteur {
       background-color: var(--custom-primary) !important;
   }
   ```

### Structure des fichiers

- **`variables.css`** : Variables CSS centralisées
- **`custom.css`** : Styles de personnalisation
- **`email_templates.xml`** : Styles pour les emails
- **`color_config.xml`** : Configuration système

## 🔍 Débogage

### Technique d'identification des éléments violets

Ajoutez temporairement ce code dans `custom.css` pour faire clignoter les éléments violets :

```css
@keyframes highlight-purple {
    0% { border: 3px solid red; }
    50% { border: 3px solid yellow; }
    100% { border: 3px solid red; }
}

*[style*="#875A7B"] {
    animation: highlight-purple 1s infinite !important;
}
```

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. **Fork le projet**
2. **Créez une branche pour votre fonctionnalité**
   ```bash
   git checkout -b feature/nouvelle-fonctionnalite
   ```
3. **Committez vos changements**
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. **Push vers la branche**
   ```bash
   git push origin feature/nouvelle-fonctionnalite
   ```
5. **Ouvrez une Pull Request**

## 📋 Compatibilité

- **Odoo 18.0** ✅ Testé et validé
- **Odoo 17.0** ⚠️ Devrait fonctionner (non testé)
- **Odoo 16.0** ⚠️ Adaptations possibles requises

## 📝 Changelog

### Version 1.0.0
- ✅ Remplacement couleur principale Odoo
- ✅ Support des emails automatiques
- ✅ Badges et tags personnalisés
- ✅ Interface backend/frontend

## ⚖️ Licence

Ce projet est sous licence LGPL-3. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

**Auxil HOUESSOU**
- Email: info@auxilhouessou.com
- GitHub: [@Garconposey](https://github.com/Garconposey)

## 🐛 Signaler un problème

Si vous rencontrez des problèmes ou avez des suggestions :
1. **Vérifiez les [issues existantes](https://github.com/Garconposey/custom-theme-color-odoo/issues)**
2. **Créez une nouvelle issue** avec :
   - Description du problème
   - Capture d'écran si applicable
   - Version d'Odoo utilisée
   - Navigateur et version

## 💡 Support

- **Documentation** : Ce README
- **Issues GitHub** : Pour les bugs et fonctionnalités
- **Discussions** : Pour les questions générales

---

⭐ **Si ce module vous aide, n'hésitez pas à lui donner une étoile !**