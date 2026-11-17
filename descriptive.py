import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from outils import charger_donnees

df = charger_donnees()
print(df.shape)

# Financement
Fbar = df["funding_total_usd"].mean()
print(f"Moyenne du financement \nFbar = {Fbar}\n")

Mf = df["funding_total_usd"].median()
print(f"Médiane du financement \nMf = {Mf}\n")

sigma_F = df["funding_total_usd"].std(ddof=0)
print(f"Écart type du financement \nsigma_F = {sigma_F}\n")

# Taille de l'équipe
Ebar = df["relationships"].mean()
print(f"Moyenne du taille de l'équipe \nEbar = {Ebar}\n")

Me = df["relationships"].median()
print(f"Médiane du taille de l'équipe \nMe = {Me}\n")

sigma_E = df["relationships"].std(ddof=0)
print(f"Écart type du taille de l'équipe \nsigma_E = {sigma_E}\n")

# Taux de succès
Tbar = df["labels"].mean()
print(f"Moyenne du taux de succès \nTbar = {Tbar}\n")

Mt = df["labels"].median()
print(f"Médiane du taux de succès \nMt = {Mt}\n")

sigma_T = df["labels"].std(ddof=0)
print(f"Écart type du taux de succès \nsigma_T = {sigma_T}\n")

# Écarts entre pays
groupe_etats = df.groupby("state_group")["labels"]

moyenne_etats = groupe_etats.mean()
print(moyenne_etats)

etendue_etats = moyenne_etats.max() - moyenne_etats.min()
std_etats = moyenne_etats.std(ddof=0)

print(f"\nÉtendue des taux par État {etendue_etats}\n")
print(f"Écart-type des taux par État {std_etats}\n")

# Écarts entre categorie
groupe_categorie = df.groupby("category_group")["labels"]

moyenne_categorie = groupe_categorie.mean()
print(moyenne_categorie)

etendue_categorie = moyenne_categorie.max() - moyenne_categorie.min()
std_categorie = moyenne_categorie.std(ddof=0)

print(f"\nÉtendue des taux par secteur {etendue_categorie}\n")
print(f"Écart-type des taux par secteur {std_categorie}\n")

# Nombre de startups rachetées par État
rachetees = df[df["labels"] == 1]
compte_rachetees = rachetees["state_group"].value_counts()
plt.bar(list(compte_rachetees.index), list(compte_rachetees.values))
plt.title("Nombre de startups rachetées par État")
plt.xlabel("État")
plt.ylabel("Nombre de startups rachetées")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/barres_rachetees_etats.png")
plt.show()

# Taux de succès par État
taux_etats = moyenne_etats.sort_values(ascending=False)
plt.bar(list(taux_etats.index), list(taux_etats.values))
plt.title("Taux de succès par État")
plt.xlabel("État")
plt.ylabel("Taux de succès")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/barres_taux_etats.png")
plt.show()

# Histogramme du financement
plt.hist(df["funding_total_usd"], bins=30)
plt.title("Répartition du financement total")
plt.xlabel("Financement total (dollars)")
plt.ylabel("Nombre de startups")
plt.savefig("figures/hist_financement.png")
plt.show()

# Histogramme du logarithme du financement
plt.hist(df["log_funding"], bins=30)
plt.title("Répartition du logarithme du financement total")
plt.xlabel("Logarithme du financement total")
plt.ylabel("Nombre de startups")
plt.savefig("figures/hist_log_financement.png")
plt.show()

# Histogramme de la taille d'équipe
plt.hist(df["relationships"], bins=30)
plt.title("Répartition de la taille d'équipe")
plt.xlabel("Nombre de relations")
plt.ylabel("Nombre de startups")
plt.savefig("figures/hist_relationships.png")
plt.show()