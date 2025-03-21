# Advanced CLI Task Manager

## Description

Ce projet est un gestionnaire de tâches en ligne de commande (CLI) implémenté en Python.  
Il permet d'ajouter, de lister et de supprimer des tâches via des sous-commandes.  
Les tâches sont stockées dans un fichier JSON et toutes les actions sont consignées dans un fichier de log.  
Le chemin du fichier des tâches peut être configuré via la variable d'environnement `TASKS_FILE_PATH`.

## Fonctionnalités

- **Ajouter une tâche** : Ajouter une nouvelle tâche avec une description et une priorité.
- **Lister les tâches** : Afficher la liste de toutes les tâches enregistrées.
- **Supprimer une tâche** : Supprimer une tâche par son ID.
- **Logging** : Toutes les actions (ajout, suppression, etc.) sont enregistrées dans `logs/task_manager.log`.
- **Configuration via variable d'environnement** : Utilisation de `TASKS_FILE_PATH` pour définir le chemin du fichier JSON des tâches.
- **Tests Unitaires** : Tests pour les fonctions `add_task()` et `delete_task()`.

## Structure du Projet

#### Voici la structure des répertoires et fichiers du projet :

```plaintext
advanced_cli_task_manager/
├── task_manager/           # Code source du CLI Task Manager
│   ├── __init__.py
│   ├── cli.py              # Point d'entrée CLI
│   ├── core.py             # Logique métier (gestion des tâches)
│   ├── logger.py           # Configuration du logging
│   └── config.py           # Gestion de la configuration (variables d'environnement)
├── tests/                  # Tests unitaires
│   └── test_core.py
├── tasks.json              # Fichier JSON pour stocker les tâches
├── requirements.txt        # Dépendances
└── Readme.md               # Documentation du projet
```

---

## Utilisation

### Ajouter une Tâche
Pour ajouter une tâche avec une description et une priorité, utilisez la commande suivante :

```bash
python3 -m task_manager.cli add "Acheter des provisions" --priority 2
```

### Lister les Tâches
Pour afficher la liste des tâches enregistrées :


```bash
python3 -m task_manager.cli list
```

### Supprimer une Tâche
Pour supprimer une tâche en précisant son ID :

```bash
python3 -m task_manager.cli delete 1
```


### Exécution des Tests Unitaires
Pour lancer les tests unitaires, exécutez :

```bash
python3 -m unittest tests/test_core.py
```

Vous devriez obtenir un résultat similaire à :

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```