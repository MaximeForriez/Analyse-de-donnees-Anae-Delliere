#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("data/resultats-elections-presidentielles-2022-1er-tour.csv", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)
    print(contenu)

#Question 5
colonnes_quanti = [
    col for col in contenu.columns
    if contenu[col].dtype in ["int64", "float64"]]
print("Colonnes quantitatives :", colonnes_quanti)

moyennes = contenu[colonnes_quanti].mean().round(2).tolist()
medianes = contenu[colonnes_quanti].median().round(2).tolist()
modes = contenu[colonnes_quanti].mode().iloc[0].round(2).tolist()
ecarts_type = contenu[colonnes_quanti].std().round(2).tolist()
ecart_abs_moyenne = (
        np.abs(contenu[colonnes_quanti] - contenu[colonnes_quanti].mean())
    .mean()
    .round(2)
    .tolist()
)
etendue = (
    (contenu[colonnes_quanti].max() - contenu[colonnes_quanti].min())
    .round(2)
    .tolist()
)
#Question 6 
print("Moyennes :", moyennes)
print("Médianes :", medianes)
print("Modes :", modes)
print("Écarts type :", ecarts_type)
print("Écarts absolus à la moyenne :", ecart_abs_moyenne)
print("Étendues :", etendue)

#Question 7 
# Distance interquartile : Q3 - Q1
IQR = (
    contenu[colonnes_quanti].quantile(0.75)
    - contenu[colonnes_quanti].quantile(0.25)
).round(2).tolist()

# Distance interdécile : D9 - D1
IDR = (
    contenu[colonnes_quanti].quantile(0.90)
    - contenu[colonnes_quanti].quantile(0.10)
).round(2).tolist()

print("Distance interquartile (IQR) :", IQR)
print("Distance interdécile (IDR) :", IDR)

#Question 8 
import os
dossier = "img"
if not os.path.exists(dossier):
    os.makedirs(dossier)
for col in colonnes_quanti:
    plt.figure(figsize=(6, 4))
    plt.boxplot(contenu[col].dropna(), vert=True)
    
    plt.title(f"Boîte à moustaches – {col}")
    plt.ylabel("Valeurs")
    
    # Enregistrement
    plt.savefig(f"img/{col}.png")
    plt.close()

# Question 10 
with open("data/island-index.csv", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)
    print(contenu)

#Question 11

# Vérifier les colonnes disponibles
print(contenu.columns)
surface = contenu["Surface (km²)"]

# Définir les intervalles
bins = [0, 10, 25, 50, 100, 2500, 5000, 10000, float("inf")]
labels = [
    "]0;10]",
    "]10;25]",
    "]25;50]",
    "]50;100]",
    "]100;2500]",
    "]2500;5000]",
    "]5000;10000]",
    "]10000;+∞["
]

# Catégoriser les surfaces
contenu["Categorie"] = pd.cut(surface, bins=bins, labels=labels, right=True)

# Compter le nombre d’îles par catégorie
counts = contenu["Categorie"].value_counts().sort_index()

print(counts)




# Sources des données : production de M. Forriez, 2016-2023