from outils import charger_donnees

df = charger_donnees()

print("Dimensions :", df.shape)
print(df.head())
print(df["labels"].value_counts())
print(df.isna().sum())

print("\n========== VÉRIFICATION ==========")

print("Dimensions du fichier :", df.shape)

print("\nRépartition de la variable labels :")
print(df["labels"].value_counts())

print("\nValeurs manquantes :")
print(df.isna().sum())