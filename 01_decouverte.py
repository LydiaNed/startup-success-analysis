import pandas as pd

# On charge le csv
df = pd.read_csv("data/startup data.csv")

pd.set_option("display.max_columns", None)
# on regarde combien de lignes et colonnes
print(f"Nombre de lignes et colonnes : {df.shape}\n")

# on regarde les colonnes
print("Colonnes")
print(df.columns)

# 5 premiers lignes - à quoi ça ressemble
print(df.head())

# chaque colonne et son type
print(df.info())

# combien de startups acquired et closed ?
print(df["status"].value_counts())

# Si acquired va toujours avec 1 et closed avec 0
print(pd.crosstab(df["status"], df["labels"]))
print()

# nombre de dates de fermeture présentes pour comparer au nombre de closed
print(f"Nombre des dates de ferméture non vides : {df["closed_at"].notna().sum()}\n")

# On a 335 date de fermeture non vides alors que 'status' montre 326. On a donc 9 dates en trop

# on verifie si state_code.1 est vraiment une copie
print((df["state_code"] == df["state_code.1"]).sum())
print()

# On trouve 922 valeurs identiques donc oui

# comparaison age_first_milestone_year à milestones. Si 1 ou plusieurs milestones et pas de age_first_milestone_year
print(df[df["age_first_milestone_year"].isna()]["milestones"].describe())
print()
# min et max valent 0 donc ces startups n'ont aucun milestones


# minimum, maximum et moyenne des colonnes numériques
print(df.describe())
# min age_first_funding_year, age_last_funding_year, age_first_milestone_year, age_last_milestone_year, negatives

# Les 9 dates de fermeture en trop
print(df[(df["closed_at"].notna()) & (df["status"] == "acquired")])
print()

# age negative
print((df["age_first_funding_year"] < 0).sum())
print((df["age_last_funding_year"] < 0).sum())
print((df["age_first_milestone_year"] < 0).sum())
print((df["age_last_milestone_year"] < 0).sum())
print()

# is_CA est-elle une copie de state_code
print((df["is_CA"] == (df["state_code"] == "CA")).all())
print((df["is_software"] == (df["category_code"] == "software")).all())

print((df["is_CA"] != (df["state_code"] == "CA")).sum())
print(df[df["is_CA"] != (df["state_code"] == "CA")][["name", "city", "state_code", "state_code.1", "is_CA"]])

propre = pd.read_csv("data/propre.csv", parse_dates=["founded_at", "closed_at", "first_funding_at", "last_funding_at"])
print(propre.shape)
print(propre.dtypes)