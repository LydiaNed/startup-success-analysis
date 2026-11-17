# Projet Startups : analyse de la réussite

Analyse de 922 startups (dataset Kaggle « Startup Success Prediction ») : statistiques descriptives, corrélations, régression logistique et ACP.

## Installation
```
python3 -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```
Dans VS Code : *Select Interpreter* puis choisir celui de `.venv`.

## Bibliothèques utilisées et à quoi elles servent

| Bibliothèque | Sert à | Parties du sujet |
|---|---|---|
| `pandas` | lire et manipuler le tableau (colonnes, filtres, regroupements, `get_dummies`) | toutes |
| `numpy` | calculs sur des nombres : moyennes, écarts-types, matrices, valeurs propres, logarithme | descriptive, corrélation, ACP |
| `matplotlib` | graphiques de base : histogrammes, barres, nuages de points, cercle des corrélations, plan factoriel | toutes les parties avec graphique |
| `seaborn` | graphiques plus rapides à écrire : heatmap de la matrice de corrélation | corrélation |
| `scikit-learn` | régression logistique, séparation entraînement/test (`train_test_split`), précision, matrice de confusion | régression logistique (modèle et évaluation) |

Les autres lignes de `requirements.txt` sont des dépendances installées automatiquement : inutile d'y toucher.

Si quelqu'un a besoin d'une autre bibliothèque : l'installer avec `pip install ...`, relancer `pip freeze > requirements.txt`, ajouter une ligne dans ce tableau et prévenir le groupe.

## Contenu du dossier
- `data/startup data.csv` : données brutes, **ne jamais modifier**.
- `data/propre.csv` : données nettoyées, produites par `02_nettoyage.py`.
- `01_decouverte.py` : exploration du fichier brut (on regarde, on ne modifie pas).
- `02_nettoyage.py` : nettoyage ; relancer pour régénérer `data/propre.csv`.
- `outils.py` : fonction `charger_donnees()`.
- `notes_donnees.md` : observations, décisions de nettoyage et dictionnaire des colonnes. **À lire avant de commencer.**
- `figures/` : graphiques en PNG (un par fichier, nom clair).
- `texte/` : le paragraphe de chacun pour le rapport, avec la question de réflexion stratégique de chaque graphique.

## Charger les données
```python
from outils import charger_donnees
df = charger_donnees()
```

## Règles communes
- Tout le monde part de `data/propre.csv`, jamais du fichier brut.
- Chacun travaille dans **son propre fichier** pour ne jamais modifier le même fichier à deux.
- Un fichier par partie : descriptive.py, correlation.py, regression_logistique.py, evaluation_logistique.py, acp.py
- Succès = `labels` (1 = rachetée, 0 = fermée). `closed_at` et `status` ne servent jamais de variables explicatives.
- Pays = État américain : utiliser `state_group` (États de plus de 15 startups, les autres dans « Autres »).
- Secteur : utiliser `category_group`, même règle.
- Taille de l'équipe = `relationships` (le dataset n'a pas d'effectif).
- Âge = `age_last_funding_year` (âge de la startup à son dernier financement). Négatif pour certaines startups : voir `dates_incoherentes`.
- Financement : `funding_total_usd` pour les moyennes, `log_funding` pour les graphiques, la corrélation et l'ACP.
- Startups à dates incohérentes (`dates_incoherentes` = 1, 83 lignes) : chacun décide de les garder ou de les écarter, et le dit dans son paragraphe.
- Pour les modèles, créer les colonnes 0/1 des États avec `pd.get_dummies`, en gardant « Autres » comme groupe de référence.
- Même graine aléatoire partout : `random_state=42`.
- Chaque graphique est accompagné d'une question de réflexion orientée décision stratégique.

## Répartition
(à compléter : qui fait quoi, dates internes)

Esteban: Partie 1: 2.2, 3.1, 3.1 
          Gestion redaction et presentation finale de la partie 1
          Gestion redaction des rendus du projet (rapport et presentation)
