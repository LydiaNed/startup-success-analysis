
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss

from outils import charger_donnees



df = charger_donnees()
print(df.columns.tolist())

print("Dimensions :", df.shape)
print("\nRépartition des startups :")
print(df["labels"].value_counts())

# 2. Préparation des variables explicatives

# Variables quantitatives
quant = ["log_funding", "relationships"]

# Transformer la variable géographique en variables binaires
dummies_etat = pd.get_dummies(
    df["state_group"],
    prefix="etat",
    dtype=int
)

print("\nColonnes géographiques créées :")
print(dummies_etat.columns.tolist())

# Garder "Autres" comme catégorie géographique de référence
dummies_etat = dummies_etat.drop(columns="etat_Autres")

# Construire la matrice des variables explicatives
X = pd.concat([df[quant], dummies_etat], axis=1)

# Définir la variable cible
y = df["labels"]

print("\nDimensions de X :", X.shape)
print("Dimensions de y :", y.shape)

print("\nAperçu des variables explicatives :")
print(X.head())

# 3. Séparation des données

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Taille de l'ensemble d'entraînement :", X_train.shape)
print("Taille de l'ensemble de test :", X_test.shape)

print("\nRépartition dans l'entraînement :")
print(y_train.value_counts())

print("\nRépartition dans le test :")
print(y_test.value_counts())

# 4. Standardisation des variables quantitatives

scaler = StandardScaler()

# Copies des ensembles de données
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

# Apprendre la standardisation sur l'entraînement
X_train_scaled[quant] = scaler.fit_transform(X_train[quant])

# Appliquer la même transformation au test
X_test_scaled[quant] = scaler.transform(X_test[quant])

print("Moyennes après standardisation :")
print(X_train_scaled[quant].mean())

print("\nÉcarts-types après standardisation :")
print(X_train_scaled[quant].std())
# 5. Entraînement du modèle

modele = LogisticRegression(
    random_state=42,
    max_iter=1000
)

modele.fit(X_train_scaled, y_train)

print("Modèle entraîné avec succès !")
# 6. Prédictions

y_pred = modele.predict(X_test_scaled)

print("Prédictions du modèle :")
print(y_pred)

print("\nValeurs réelles :")
print(y_test.values)
# 7. Évaluation du modèle

accuracy = accuracy_score(y_test, y_pred)

probabilites = modele.predict_proba(X_test_scaled)

loss = log_loss(y_test, probabilites)

print("Accuracy :", accuracy)
print("Log Loss :", loss)

# 8. Analyse des coefficients

coefficients = pd.DataFrame({
    "Variable": X.columns,
    "Coefficient": modele.coef_[0]
})

print(coefficients.sort_values(
    by="Coefficient",
    ascending=False
))

# 9. Analyse des Odds Ratios
coefficients["Odds_Ratio"] = np.exp(coefficients["Coefficient"])

print("\nAnalyse des Odds Ratios :")
print(
    coefficients.sort_values(
        by="Odds_Ratio",
        ascending=False
    ).round(3)
)


from sklearn.metrics import confusion_matrix, classification_report

# 10. Matrice de confusion
matrice = confusion_matrix(y_test, y_pred)

print("\nMatrice de confusion :")
print(matrice)

# 11. Rapport de classification
print("\nRapport de classification :")
print(classification_report(y_test, y_pred))

