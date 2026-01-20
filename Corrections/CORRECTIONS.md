# Élements de corrections

## Séance 2.

### Questions

- **Question 8.** Vous ne répondez pas la question sur la hiérarchie.

### Code

- **Question 11.** Point de détail ! Pour exécuter votre code, j'ai dû remplacer `dept = contenu.loc[i, "Libellé du département"]` par `dept = contenu.loc[i, "Code du département"]` pour faire fonctionner votre code.

## Séance 3.

### Questions

- **Question 5.** Il manque les déciles.

### Code

- Excellent !

## Séance 4

### Questions

- **Question 5.** Une statistique travaillant sur la population totale est une statistique  exhaustive, et non une enquête exhaustive qui est la méthode de la collecte des données.

### Code

- Excellent !

## Séance 5

### Questions

- Excellent !

### Code

- Excellent !

- La distribution test1 est normale. Il y a un problème avec le calcul de votre *p-value*.

## Séance 6

### Questions

- Il manque quelques éléments.

### Code

- **Question 7.** Il n'est pas possible de calculer les tests avec un seul classement. Il en faut au moins deux.

- Il y a une erreur au niveau du calcul des tests. Vous avez écrit :

```
    #14 Calcul du coefficient de corrélation de Spearman
    spearman_corr, spearman_pvalue = spearmanr(colonne_pop, colonne_dens)

    # Calcul du coefficient de concordance de Kendall
    kendall_corr, kendall_pvalue = kendalltau(colonne_pop, colonne_dens)
```

Il aurait fallu écrire quelque chose comme :

```
    #14 Calcul du coefficient de corrélation de Spearman
    spearman_corr_pop, spearman_pvalue_pop = spearmanr(colonne_pop_2007, colonne_pop_2025)

    # Calcul du coefficient de concordance de Kendall
    kendall_corr_dens, kendall_pvalue_dens = kendalltau(colonne_dens_2007, colonne_dens_2025)
```

## Humanités numériques

- Analyse trop superficielle.

## Remarques générales

- Aucun dépôt régulier sur `GitHub`.

- Attention ! Vous devez appeler votre fichier de code `main.py`. Vous comprendrez si vous faites un jour du `Python` avancé.
