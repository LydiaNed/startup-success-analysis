import numpy as np
import matplotlib.pyplot as plt
from outils import charger_donnees

df = charger_donnees()

# on enlève les startups où age_last_funding_year est négatif
# (dernier financement daté avant la création = date fausse), 13 lignes, il en reste 909
df = df[df["age_last_funding_year"] >= 0]

# variables pour l'acp
# log_funding = financement (en log car montants très étalés)
# relationships = taille de l'équipe, pas d'effectif dans le dataset
# age_last_funding_year = âge
# milestones = à la place de la valorisation qui existe pas
# labels on le met pas dans le calcul (c'est 0/1), on s'en sert juste pour la couleur
# pas funding_rounds (doublon avec le financement) ni avg_participants (on sait pas trop ce que c'est)
colonnes = ["log_funding", "relationships", "age_last_funding_year", "milestones"]

# centrage et réduction : (X - moyenne) / écart-type

X = df[colonnes].to_numpy() #on passe colonnes en matrice et on met la matrice dans la varible X 
moyenne = X.mean(axis=0) #axis=0 calcule verticalement, en descendant le long des lignes sans lui, numpy fait une seule moyenne pour toute la matrice
ecart_type=X.std(axis=0) #pareil pour axis 0 
X_cr = (X - moyenne) / ecart_type #X_cr = matrice X centrer et reduit 

R= (1/X_cr.shape[0]) * X_cr.T @ X_cr     # on calcule la matrice de corrélation : (1/n) * XTX  avec X_cr.shape[0] qui donne n       et X_cr.T qui donne la transposé de la matrice X
print(R.shape)
print(np.round(R, 2))
print(np.round(np.corrcoef(X, rowvar=False), 2))

# calcul des lambda (valeurs propres) = combien d'info chaque axe garde



valeurs, vecteurs = np.linalg.eigh(R)  # eigh renvoie les lambda et les vecteurs, on les récupère dans 2 variables




#pourquoi on va remetre dans l'ordre :
# eigh donne les lambda du plus petit au plus grand
# mais en acp l'axe 1 doit être celui qui garde le plus d'info, puis l'axe 2 etc
# si on trie pas, notre "axe 1" serait le moins important et tout le reste serait faux
# (le cercle et le plan factoriel prendraient les mauvais axes)
# chaque vecteur va avec son lambda donc on range les vecteurs dans le même ordre

ordre = np.argsort(valeurs)[::-1]  # positions des lambda du plus grand au plus petit
valeurs = valeurs[ordre]  # lambda du plus grand au plus petit, le plus grand = axe 1
vecteurs = vecteurs[:, ordre]  # pareil pour les vecteurs (une colonne = un axe)
print(valeurs)


vecteurs[:, 0] = -vecteurs[:, 0]# on inverse l'axe 1 pour que à droite = grosse startup, le signe d'un vecteur propre change rien


# % d'info de chaque axe et le cumul
inertie = valeurs / valeurs.sum() * 100
print(np.round(inertie, 1))
print(np.round(np.cumsum(inertie), 1)) 
# lambda = [1.72 1.41 0.46 0.41], en % d'info = [43 35.2 11.5 10.3], axes 1 et 2 ensemble = 78 %

# petite recap , on a donc avec kaiser     que lambda 1 = 1.72  lambda 2 = 1.41
# ils explique 43 + 35.2 = 78% a eux 2 
#il y a une grosse chute après l’axe 2 (de 1,41 à 0,46), puis presque rien entre 0,46 et 0,41.

#maintenant les coordonnées des startups  Z=X*V      V= matrice vecteur    X c'est la matrice X_cr

Z= X_cr @ vecteurs   # position de chaque startup sur chaque axe
print(Z.shape)  # on obtient une matrice (909, 4)  chaque ligne est une startup chaque colonne est sa position sur un axe (colonne 0 = axe 1, colonne 1 = axe 2…).
# j'ai calculé les 4 axes mais j'utilise que les colonnes 0 et 1 (axes 1 et 2), les axes 3 et 4 apportent peu d'info (22 %) d'après kaiser car lambda inférieur a 1


# corrélations entre les variables et les axes (√lambda × vecteur)
# ça sert pour tracer les flèches du cercle des corrélations
correlations = vecteurs * np.sqrt(valeurs)
print(np.round(correlations[:, :2], 2))  # que les axes 1 et 2

# ça nous donne
#                  axe 1   axe 2
# financement      0.77    0.43
# relationships    0.76   -0.44
# âge              0.52    0.72
# milestones       0.53   -0.71

# éboulis : les 4 lambda en barres, la ligne rouge = kaiser (lambda = 1)
plt.bar([1, 2, 3, 4], valeurs)
plt.axhline(1, color="red", linestyle="--")
plt.xlabel("axe")
plt.ylabel("lambda")
plt.title("éboulis des valeurs propres")
plt.savefig("figures/acp_eboulis.png", dpi=150, bbox_inches="tight")
plt.close()
#on voit clairement que il faut garder que lambda 1 et 2

#pour le cercle de correlation , C’est un dessin du tableau de corrélations. Chaque variable devient une flèche qui part du centre 

fig, ax = plt.subplots(figsize=(6, 6))  # une figure carrée, ax = la zone où on dessine  fig= la figure entiere

cercle = plt.Circle((0, 0), 1, fill=False)  # cercle de centre (0,0), rayon 1, pas rempli
ax.add_patch(cercle)  # on le pose sur le dessin

noms = ["financement", "relationships", "âge", "milestones"]
for i in range(4):  # i = 0, 1, 2, 3 : une fois par variable
    x = correlations[i, 0]  # son chiffre sur l'axe 1 (va à droite)
    y = correlations[i, 1]  # son chiffre sur l'axe 2 (va en haut ou en bas)
    ax.arrow(0, 0, x, y, head_width=0.03)  # flèche qui part de (0,0) et va jusqu'à (x, y)
    ax.text(x, y, noms[i])  # on écrit le nom de la variable au bout
ax.set_xlim(-1.2, 1.5)  # un peu plus large à droite pour que les noms tiennent
ax.set_ylim(-1.1, 1.1)  # pareil en hauteur
ax.set_aspect("equal")  # sinon le cercle est écrasé en ovale
ax.set_xlabel(f"axe 1 ({inertie[0]:.1f} %)")
ax.set_ylabel(f"axe 2 ({inertie[1]:.1f} %)")
ax.set_title("cercle des corrélations")
plt.savefig("figures/acp_cercle.png", dpi=150, bbox_inches="tight")
plt.close()


# plan factoriel : chaque point = une startup, placée selon ses coordonnées sur les axes 1 et 2
# couleur = rachetée (succès) ou fermée (échec)
succes = df["labels"].to_numpy()  # 1 = rachetée, 0 = fermée (même ordre que Z car même df filtré)

fig, ax = plt.subplots(figsize=(7, 6))

# on trace les fermées puis les rachetées, chacune avec sa couleur
ax.scatter(Z[succes == 0, 0], Z[succes == 0, 1], s=10, alpha=0.5, color="red", label="fermée")
ax.scatter(Z[succes == 1, 0], Z[succes == 1, 1], s=10, alpha=0.5, color="green", label="rachetée")

ax.axhline(0, color="grey", linewidth=0.5)  # ligne horizontale au milieu
ax.axvline(0, color="grey", linewidth=0.5)  # ligne verticale au milieu
ax.set_xlabel(f"axe 1 ({inertie[0]:.1f} %) : taille de la startup")
ax.set_ylabel(f"axe 2 ({inertie[1]:.1f} %) : âge (haut) / milestones (bas)")
ax.set_title("plan factoriel des startups")
ax.legend()
plt.savefig("figures/acp_plan.png", dpi=150, bbox_inches="tight")
plt.close()


# taux de rachat par zone du plan
gauche = Z[:, 0] < 0
bas = Z[:, 1] < 0
print("gauche", gauche.sum(), succes[gauche].mean())
print("droite", (~gauche).sum(), succes[~gauche].mean())
print("haut gauche", (gauche & ~bas).sum(), succes[gauche & ~bas].mean())
print("bas droite", (~gauche & bas).sum(), succes[~gauche & bas].mean())



# pour conclure
# acp_eboulis.png : ça montre combien d'axes on garde, on garde que les 2 premiers (lambda > 1, 78 % de l'info)
# acp_cercle.png : c'est  la légende, ça dit ce que veut dire être à droite ou en haut
#   à droite = startup qui a beaucoup d'argent et de réseau (axe 1 = la taille)
#   en haut = startup plus vieille, en bas = startup avec beaucoup de milestones (axe 2 = mature ou dynamique)
# acp_plan.png : c'est la carte avec toutes les startups, vert = rachetée rouge = fermée
#   les vertes sont plutôt à droite et en bas, les rouges plutôt à gauche
#   donc les grosses startups qui avancent vite réussissent plus, mais au milieu c'est mélangé donc c'est pas garanti