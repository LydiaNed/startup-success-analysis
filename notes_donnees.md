# Notes sur les données

Fichier brut : `data/startup data.csv` (jamais modifié). Fichier propre : `data/propre.csv`, produit par `02_nettoyage.py`.

## 1. Observations (ce qu'on a vu dans le fichier brut)

### Taille et types
- 923 lignes (startups) et 49 colonnes.
- Les dates (`founded_at`, `closed_at`, `first_funding_at`, `last_funding_at`) sont lues comme du texte.
- `funding_total_usd`, `funding_rounds`, `relationships` : aucune valeur manquante.

### Colonnes en trop
- `Unnamed: 0`, `id`, `object_id` : numéros de ligne ou identifiants, sans information utile.
- `Unnamed: 6` : texte qui répète ville + État + code postal ; 430 valeurs présentes, 493 manquantes.
- `state_code.1` : copie de `state_code` (922 lignes identiques sur 923) ; 1 valeur manquante (Cuil).
- `is_CA`, `is_NY`, `is_MA`, `is_TX`, `is_otherstate` : copies de `state_code` en 0/1. Vérifié : `is_CA` ≠ (`state_code` == "CA") pour 1 seule ligne, Cuil, dont `state_code.1` est vide (donc `is_CA` = 0 alors que l'État est CA).
- `is_software`, `is_web`, `is_mobile`, `is_enterprise`, `is_advertising`, `is_gamesvideo`, `is_ecommerce`, `is_biotech`, `is_consulting`, `is_othercategory` : copies de `category_code` en 0/1. Vérifié pour `is_software` : identique à (`category_code` == "software") sur toutes les lignes.
- `latitude`, `longitude`, `zip_code` : valeurs incohérentes. Exemples : Bandsintown (San Diego, CA) a les coordonnées de Boston ; N2N Commerce (Cambridge, MA) a celles du centre des États-Unis ; Brightkite (Burlingame, CA) celles de Denver ; Heartscape a « Maryland 21045 » dans `zip_code`.
- Absent par rapport au sujet : pas de nombre d'employés, pas de valorisation.

### Cible : succès ou échec
- `status` et `labels` disent la même chose : 597 `acquired` = `labels` 1, 326 `closed` = `labels` 0, aucun autre croisement.
- `labels` : moyenne 0,6468, soit 64,7 % de succès.
- Toutes les startups sont soit rachetées, soit fermées : aucune « encore en activité ». Dans ce dataset, « succès » veut dire « rachetée ».

### Cases vides
- `closed_at` : 335 dates présentes, 588 vides (vide = pas de fermeture).
- `age_first_milestone_year` et `age_last_milestone_year` : 771 présentes, 152 vides chacune. Ces 152 startups ont `milestones` = 0 (min = max = 0, vérifié), donc il n'y a rien à dater.

### `closed_at` : 9 dates en trop
- 335 dates de fermeture, mais seulement 326 startups `closed` : 9 startups `acquired` ont une date de fermeture.
- Hypothèse plausible : elles ont été rachetées, puis leur service a fermé. `closed_at` veut donc dire « a fermé à cette date », pas « a échoué ».
- Une est franchement incohérente : adBrite a `closed_at` = 2/1/2001 alors que `founded_at` = 1/1/2003 (fermée avant d'être créée).

### Âges négatifs
- Nombre de startups avec un âge négatif : `age_first_funding_year` 46 (min −9,05) ; `age_last_funding_year` 13 (min −9,05) ; `age_first_milestone_year` 46 (min −14,17) ; `age_last_milestone_year` 12 (min −7,01).
- Un âge négatif veut dire que l'événement est daté d'avant la création de la startup, ce qui est impossible. Exemple : Aardvark a `founded_at` = 7/1/2007 mais un premier financement le 1/1/2007 (`age_first_funding_year` = −0,4959).
- On ne peut pas savoir si c'est la date de création ou la date de l'événement qui est fausse, ni retrouver la vraie valeur.
- Au total, 83 startups ont au moins un âge négatif.

### Financement et équipe
- `funding_total_usd` : moyenne ≈ 25,4 millions, médiane 10 millions, minimum 11 000 $, maximum 5,7 milliards. Quelques startups énormes tirent la moyenne vers le haut.
- `relationships` : de 0 à 63, médiane 5. Elle sera notre remplaçant de la taille d'équipe.

### Doublons et répartition (après nettoyage partiel)
- 1 ligne en double (identique sur toutes les colonnes restantes, même nom de startup).
- Les États : 35 valeurs, la Californie en a 487 sur 922 (53 %) ; 11 États n'ont qu'une ou deux startups.
- Les secteurs : 34 valeurs, de `software` (153) à `sports` (1) ; 18 secteurs ont moins de 15 startups.

## 2. Décisions (ce qu'on a choisi)

### Étape 1 : colonnes inutiles
- `Unnamed: 0`, `id`, `object_id` : retirées, ce sont des numéros ou des identifiants sans information utile.
- `Unnamed: 6` : retirée, texte qui répète ville + État + code postal.
- `state_code.1` : retirée, copie de `state_code` (922 lignes identiques sur 923).
- `latitude`, `longitude`, `zip_code` : retirées, valeurs incohérentes. Le sujet demande le pays (ici l'État), `state_code` suffit.
- `status` : retirée, `labels` dit la même chose et sert de cible.
- `is_top500` : retirée, sens inconnu et non demandée par le sujet.

### Étape 2 : copies et `city`
- Copies `is_...` retirées : mêmes informations que `state_code` et `category_code` (vérifié), plus lisible pour le groupe. `state_code` est plus fiable : `is_CA` se trompe pour Cuil, dont `state_code.1` est vide.
- `city` retirée : non demandée par le sujet (qui parle du pays, ici l'État) et trop de valeurs différentes pour servir de variable.

### Étape 3 : conversion des dates
- `founded_at`, `closed_at`, `first_funding_at`, `last_funding_at` converties de texte en vraies dates (format mois/jour/année). Raison : on ne peut pas calculer ni comparer avec du texte. Les cases vides de `closed_at` deviennent des dates manquantes (`NaT`).

### Étape 4 : dates incohérentes
- Colonne `dates_incoherentes` ajoutée : 1 si au moins un des quatre âges est négatif, 0 sinon. 83 startups sur 923 signalées.
- Raison : on ne peut pas retrouver la vraie date, donc on ne corrige pas et on ne supprime pas. Chaque analyse décide ensuite de garder ou d'écarter ces lignes.

### Étape 5 : doublons
- 1 ligne en double supprimée avec `drop_duplicates()` : 923 → 922 lignes.
- Raison : une startup comptée deux fois fausserait moyennes, corrélations et modèle. Après suppression, plus aucun nom n'apparaît deux fois.

### Étape 6 : cases vides
- `closed_at` : 587 cases vides, conservées. Vide = pas de date de fermeture (pas une donnée perdue). Jamais utilisée comme variable explicative.
- `age_first_milestone_year`, `age_last_milestone_year` : 152 cases vides chacune, conservées. Ce sont les startups sans milestone. On ne remplit pas avec 0 (cela voudrait dire un milestone à la création). Quiconque utilise ces colonnes dans un modèle ou une ACP devra écarter ces 152 startups ou utiliser `milestones` à la place.
- Aucune autre colonne n'a de case vide.

### Étape 7 : logarithme du financement
- Colonne `log_funding` ajoutée : logarithme népérien (`np.log`) de `funding_total_usd`. La colonne d'origine est conservée.
- Raison : les montants sont très étalés. Quelques très grosses startups écraseraient les autres sur les graphiques et dans l'ACP. Le logarithme tasse ces écarts (le maximum devient environ 2,4 fois le minimum, au lieu de 500 000 fois).
- Possible sans erreur : tous les montants sont strictement positifs (minimum 11 000).
- Chaque analyse choisit la version qui lui convient (montant d'origine pour les moyennes lisibles, `log_funding` pour les graphiques, la corrélation et l'ACP).

### Étape 8 : regroupement des États et des secteurs rares
- Deux colonnes ajoutées : `state_group` (à partir de `state_code`) et `category_group` (à partir de `category_code`). Les colonnes d'origine sont conservées.
- Règle : tout État ou secteur qui compte moins de 15 startups est regroupé dans « Autres ».
- États gardés (8) : CA, NY, MA, TX, WA, CO, IL, PA. « Autres » regroupe 27 États, soit 108 startups (environ 12 %).
- Secteurs gardés (15) : de `software` à `analytics`. « Autres » regroupe 19 secteurs (dont `other`), soit 119 startups (environ 13 %).
- Raison : avec très peu de startups par groupe, les résultats seraient dus au hasard (un coefficient de régression instable, des barres illisibles sur les graphiques).
- Le seuil de 15 est une règle pratique, pas une valeur démontrée : plus bas, les petits groupes restent peu fiables ; plus haut, « Autres » devient trop gros et mélange tout.
- À reprendre dans le rapport : la Californie représente 487 startups sur 922 (53 %), l'échantillon est dominé par un seul État.

### Étape 9 : fichier propre
- Fichier enregistré dans `data/propre.csv` (922 lignes, 27 colonnes) avec `to_csv(..., index=False)`. Le fichier brut n'est jamais modifié ; le fichier propre se régénère en relançant `02_nettoyage.py`.
- À savoir en le lisant : les dates sont du texte dans un CSV, il faut les relire avec `parse_dates=["founded_at", "closed_at", "first_funding_at", "last_funding_at"]`.

### Colonnes gardées qui ne sont pas demandées par le sujet
- `name` : gardée pour lire les résultats, pas utilisée comme variable.
- `closed_at` : gardée pour comprendre les données, jamais utilisée comme variable explicative (elle contient la réponse).
- `milestones`, `age_first_milestone_year`, `age_last_milestone_year`, `avg_participants` : gardées car peuvent être utiles pour l'ACP.

## 3. Dictionnaire des colonnes
(Les sens sont une interprétation d'après le nom des colonnes ; le fichier ne les définit pas.)

| Colonne | Type | Sens |
|---|---|---|
| `name` | texte | nom de la startup (pour lire les résultats, pas une variable) |
| `labels` | 0/1 | succès : 1 = rachetée (`acquired`), 0 = fermée (`closed`). Variable à prédire |
| `state_code` | texte | État américain de la startup |
| `state_group` | texte | `state_code`, avec les États de moins de 15 startups regroupés en « Autres » |
| `category_code` | texte | secteur d'activité |
| `category_group` | texte | `category_code`, avec les secteurs de moins de 15 startups regroupés en « Autres » |
| `founded_at` | date | date de création |
| `closed_at` | date | date de fermeture (vide si pas de fermeture). Jamais une variable explicative |
| `first_funding_at`, `last_funding_at` | date | date du premier et du dernier tour de financement |
| `age_first_funding_year`, `age_last_funding_year` | années | âge de la startup au premier et au dernier financement (négatif = date incohérente) |
| `age_first_milestone_year`, `age_last_milestone_year` | années | âge de la startup à son premier et à son dernier milestone (vide si aucun milestone) |
| `milestones` | nombre | nombre d'étapes marquantes atteintes |
| `relationships` | nombre | nombre de relations de la startup ; remplaçant de la taille d'équipe (le dataset n'a pas d'effectif) |
| `funding_rounds` | nombre | nombre de tours de financement (une levée d'argent = un tour) |
| `funding_total_usd` | dollars | total levé sur tous les tours |
| `log_funding` | nombre | logarithme népérien de `funding_total_usd` |
| `has_VC` | 0/1 | a reçu de l'argent d'un fonds de capital-risque (professionnels qui investissent l'argent de leurs clients) |
| `has_angel` | 0/1 | a reçu de l'argent d'un business angel (particulier fortuné qui investit à titre personnel, souvent très tôt) |
| `has_roundA` … `has_roundD` | 0/1 | a passé un tour de série A, B, C ou D (A = premier gros tour, puis B, C, D : montants souvent plus gros, entreprises plus avancées) |
| `avg_participants` | nombre | probablement le nombre moyen d'investisseurs par tour |
| `dates_incoherentes` | 0/1 | 1 si au moins un des quatre âges est négatif (83 startups) |