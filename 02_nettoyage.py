import pandas as pd
import numpy as np

df = pd.read_csv("data/startup data.csv")

pd.set_option("display.max_columns", None)

# on supprime des colonnes
df = df.drop(columns = ['Unnamed: 0', 'Unnamed: 6', 'state_code.1', 
                        'id', 'object_id', 'latitude', 'longitude', 
                        'zip_code', 'status', 'is_top500'])

df = df.drop(columns=['is_CA', 'is_NY', 'is_MA', 'is_TX', 
                      'is_otherstate', 'is_software', 'is_web', 'is_mobile', 
                      'is_enterprise', 'is_advertising', 'is_gamesvideo', 'is_ecommerce', 
                      'is_biotech', 'is_consulting', 'is_othercategory', 'city'])

# on convertir les dates
df["founded_at"] = pd.to_datetime(df["founded_at"], format="%m/%d/%Y")
df["closed_at"] = pd.to_datetime(df["closed_at"], format="%m/%d/%Y")
df["first_funding_at"] = pd.to_datetime(df["first_funding_at"], format="%m/%d/%Y")
df["last_funding_at"] = pd.to_datetime(df["last_funding_at"], format="%m/%d/%Y")

# Étape 4 : signaler les dates incohérentes
df["dates_incoherentes"] = (df[["age_first_funding_year",
                                "age_last_funding_year",
                                "age_first_milestone_year",
                                "age_last_milestone_year"]] < 0).any(axis=1).astype(int)

print(df["dates_incoherentes"].sum())


# Des lignes entièrement identiques
print(df.duplicated().sum())
# Le même nom plusieurs fois
print(df["name"].duplicated().sum())

# Lignes concernées (=1, Redwood Systems)
#print(df[df["name"].duplicated(keep=False)])

# On supprime le doublon
df = df.drop_duplicates()

# les cases vides
#print(df.isna().sum())

# on ajoute une colonne log_funding : log du financement
df["log_funding"] = np.log(df["funding_total_usd"])

# comment les États et les catégories se répartissent
print(df["state_code"].value_counts())
print(df["category_code"].value_counts())

# regrouper les États et catégories rares
# nombre de startups par État
counts = df["state_code"].value_counts()

# États dont le compte est au moins 15, et .index donne leurs noms (CA, NY, …) au lieu des nombres
frequents = counts[counts >= 15].index

# États avec moins de 15 startups regroupés en "Autres" (résultats peu fiables sinon)
df["state_group"] = df["state_code"].where(df["state_code"].isin(frequents), "Autres")

print(df["state_group"].value_counts())

print(df[df["state_group"] == "Autres"][["state_code", "state_group"]].head(10))

# nombre de startups par secteur
counts_cat = df["category_code"].value_counts()

# secteurs avec au moins 15 startups
frequents_cat = counts_cat[counts_cat >= 15].index

# secteurs avec moins de 15 startups regroupés en "Autres" (résultats peu fiables sinon)
df["category_group"] = df["category_code"].where(df["category_code"].isin(frequents_cat), "Autres")

print(df["category_group"].value_counts())

# on enregistre le fichier propre
df.to_csv("data/propre.csv", index=False)

print(df.shape)