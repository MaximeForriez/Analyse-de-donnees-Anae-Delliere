#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats 
from scipy.stats import spearmanr, kendalltau
import math

#Fonction pour ouvrir les fichiers
with open("data/island-index.csv", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
print(contenu)

# 3. Isoler la colonne "Surface (km2)"
surfaces = contenu["Surface (km²)"].astype(float).tolist()

# Ajouter les nouvelles valeurs (sans unité, castées en float)
surfaces.extend([
    float(85545323),  # Asie / Afrique / Europe
    float(37856841),  # Amérique
    float(7768030),   # Antarctique
    float(7605049)    # Australie
])

print("Liste des surfaces (km2) :", surfaces)

# 4. Fonction locale pour ordonner une liste en ordre décroissant
def ordreDecroissant(liste):
    return sorted(liste, reverse=True)

# 4. Ordonner la liste en ordre décroissant
surfaces_ordonnee = ordreDecroissant(surfaces)
print("Liste des surfaces ordonnée (km2) :", surfaces_ordonnee)


# 5 On suppose que surfaces_ordonnee est déjà triée en ordre décroissant
rangs = list(range(1, len(surfaces_ordonnee) + 1))

plt.figure(figsize=(8,6))
plt.plot(rangs, surfaces_ordonnee, marker="o", linestyle="-", color="blue")

plt.title("Loi rang-taille des surfaces")
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.grid(True)

plt.show()

#6 
def conversionLog(liste):
    return [np.log(x) for x in liste]

# Rangs et surfaces ordonnées
rangs = list(range(1, len(surfaces_ordonnee) + 1))
log_rangs = conversionLog(rangs)
log_surfaces = conversionLog(surfaces_ordonnee)

# Visualisation en log-log
plt.figure(figsize=(8,6))
plt.plot(log_rangs, log_surfaces, marker="o", linestyle="-", color="red")

plt.title("Loi rang-taille (échelle logarithmique)")
plt.xlabel("log(Rang)")
plt.ylabel("log(Surface en km²)")
plt.grid(True)

plt.show()

#9 Fonction pour ouvrir les fichiers
with open("data/Le-Monde-HS-Etats-du-monde-2007-2025.csv", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
print(contenu)

#10 Isoler les colonnes
colonnes = ["État", "Pop 2007", "Pop 2025", "Densité 2007", "Densité 2025"]
donnees = {col: contenu[col].astype(float).tolist() if col != "État" else contenu[col].astype(str).tolist()
           for col in colonnes}

#11 Fonction locale : prend une liste de valeurs et la liste des États associée
def ordrePopulation(valeurs, etats):
    # zip associe chaque valeur à son État
    # sorted trie par valeur décroissante
    tri = sorted(zip(valeurs, etats), key=lambda x: x[0], reverse=True)
    # On sépare à nouveau en deux listes
    valeurs_triees, etats_tries = zip(*tri)
    return list(valeurs_triees), list(etats_tries)

pop2007_triee, etats_pop2007 = ordrePopulation(donnees["Pop 2007"], donnees["État"])
pop2025_triee, etats_pop2025 = ordrePopulation(donnees["Pop 2025"], donnees["État"])
dens2007_triee, etats_dens2007 = ordrePopulation(donnees["Densité 2007"], donnees["État"])
dens2025_triee, etats_dens2025 = ordrePopulation(donnees["Densité 2025"], donnees["État"])

# Affichage pour vérifier
print("Pop 2007 triée :", pop2007_triee)
print("États correspondants :", etats_pop2007)
print("\nPop 2025 triée :", pop2025_triee)
print("États correspondants :", etats_pop2025)
print("\nDensité 2007 triée :", dens2007_triee)
print("États correspondants :", etats_dens2007)
print("\nDensité 2025 triée :", dens2025_triee)
print("États correspondants :", etats_dens2025)

# 12 Fonction locale deux classements (population et densité)
def classementPays(classement_pop, classement_dens):
    # Associer chaque État avec son rang en population et en densité
    comparaison = [(etat, classement_pop.index(etat), classement_dens.index(etat)) 
                   for etat in classement_pop]
    
    # Trier par rapport au classement de 2007 (rang population)
    comparaison.sort(key=lambda x: x[1])
    
    return comparaison

# Exemple d'utilisation avec les États triés par pop et densité en 2007
comparaison = classementPays(etats_pop2007, etats_dens2007)

# Affichage pour vérifier
print("Comparaison (État, rang Pop2007, rang Dens2007) :")
for ligne in comparaison:
    print(ligne)

# Isoler les deux colonnes sous forme de listes avec une boucle 
colonne_pop = []
colonne_dens = []

for etat, rang_pop, rang_dens in comparaison:
    colonne_pop.append(rang_pop)
    colonne_dens.append(rang_dens)

print("\nColonne Pop :", colonne_pop)
print("Colonne Dens :", colonne_dens)

from scipy.stats import spearmanr, kendalltau


#14 Calcul du coefficient de corrélation de Spearman
spearman_corr, spearman_pvalue = spearmanr(colonne_pop, colonne_dens)

# Calcul du coefficient de concordance de Kendall
kendall_corr, kendall_pvalue = kendalltau(colonne_pop, colonne_dens)

# Affichage des résultats
print("Corrélation de Spearman :", spearman_corr)
print("p-value Spearman :", spearman_pvalue)

print("\nConcordance de Kendall :", kendall_corr)
print("p-value Kendall :", kendall_pvalue)








