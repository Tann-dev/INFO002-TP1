
# TP1 Cryptologie - Compromis temps / mémoire, les tables arc-en-ciel

#### Antoine DEPOISIER & Irilind SALIHI

##### Lien Github

https://github.com/Tann-dev/INFO002-TP1

## TP

Des détails sur les commandes sont disponibles en effectuant les commandes :

```shell
python .\main.py --custom_help
python .\main.py --test_help
```

### Question 8

Si aucun décalage ne serait effectué, il se peut que l'on tomberait dans une boucle et que l'on recouvre seulement une partie de la table qui a bouclé sur elle-même.

### Question 11

Nous avons essayé avec la suite de commandes qui suit pour cracker un hash :

```shell
python .\main.py --hash --word=abcd
Empreinte de 'abcd': 81fe8bfe87576c3ecb22426f8e57847382917acf
```

```shell
python .\main.py --abc=26 --size=4 --load=crack.txt --creer_table_fichier --height=1000000 --width=10
```

```shell
python .\main.py --abc=26 --size=4 --load=crack.txt --crack --height=1000000 --width=10 --hash_to_crack=81fe8bfe87576c3ecb22426f8e57847382917acf
```

### Question 12

Dans le contexte d'une table arc-en-ciel, la complexité peut être évaluée comme O(log(hauteur) * largeur * largeur).

- La recherche dichotomique présente une complexité de log(hauteur).
- Il est nécessaire de considérer la dimension de la largeur, car en moyenne, la découverte du hash se produit à la moitié du tableau, sous réserve de sa validité et de sa correspondance avec un mot de passe répertorié dans la table. La largeur (2) intervient car à chaque itération, le recalcul du nouveau candidat à rechercher nécessite (largeur - t) itérations, soit en moyenne largeur/2 itérations.
- La complexité totale de cette recherche est exprimée comme O(hauteur) en raison du chargement de la table en mémoire.
- Les autres calculs associés demeurent en temps constant.

### Question 14

On fait déjà le test pour le premier alphabet avec un mot à quatre caractères.
Je regarde déjà la couverture de ma table, pour connaître combien de lignes, j'ai besoin à peu près.

```shell
python .\main.py --abc=26A --size=4 --stats --width=200 --height=10000
Couverture : 90.36142163436506
```

```shell
python .\main.py --abc=26A --size=4 --load=crack.txt --creer_table_fichier --height=10000 --width=200
```

```shell
python .\main.py --abc=26A --size=4 --load=crack.txt --crack --width=200 --hash_to_crack=16de25af888480da1af57a71855f3e8c515dcb61
Les résultat trouvé est : CODE
```

Le temps de calcul des tables est d'environ cinq secondes.
Le temps de calcul de l'inverse est presque instantané.


Nous essayons ensuite avec un alphabet plus grand et un nouvel alphabet.

```shell
python .\main.py --abc=40 --stats --size=5 --height=20000 --width=10000
Couverture : 71.19548044456434
```

```shell
python .\main.py --abc=40 --stats --size=5 --height=20000 --width=10000 --creer_table_fichier --load=crack.txt
```

```shell
python .\main.py --abc=40 --stats --size=5 --height=20000 --width=10000 --crack --load=crack.txt --hash_to_crack=dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2
Les résultat trouvé est : n00b.
```

Le temps de calcul des tables est d'approximativement 520 secondes, soit 8 minutes 40.
Le temps de calcul de l'inverse est d'environ 1,4 seconde.

Quand aucun n'est trouvé, il est d'environ cinq secondes.


### Question 15

Nous avons regardé avec la fonction stats, combien il faudrait de lignes dans notre table arc-en-ciel pour pouvoir avoir une couverture haute.

```shell
python .\main.py --abc=36 --size=8 --stats --width=200 --height=100000000000
Couverture : 95.33362839981649
```

On voit qu'il nous faut donc 100 000 000 000 pour pouvoir craquer quasiment tous les mots de passe.

Pour 1 000 000 il nous fallait environ 500 secondes, donc là, on a multiplié par 100 000, donc environ 50 000 000 secondes. Ce qui représente 578.7 jours. Tout cela juste pour générer la table arc-en-ciel.

Pour cracker, près de 500 000 secondes, soit 5.787 jours.

### Question 16

On garde le même TXT que celui de la question 14.

Recherche dichotomique, 1,94 secondes : 
```shell
python .\main.py --abc=40 --stats --size=5 --height=20000 --width=10000 --crack --load=crack.txt --hash_to_crack=dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2
```

Recherche exhaustive, 2.46 secondes :
```shell
python .\main.py --abc=40 --stats --size=5 --height=20000 --width=10000 --crack_exhaustive --load=crack.txt --hash_to_crack=dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2
```

### Question 17

L'ajout de sel dans le contexte des mots de passe vise à accroître la complexité du processus de hachage, ce qui rend plus difficile la tâche des attaquants cherchant à exploiter des tables arc-en-ciel pour déchiffrer les mots de passe. Le sel implique l'incorporation de caractères aléatoires au mot de passe avant son hachage. Par conséquent, même si deux utilisateurs ont le même mot de passe, le hash résultant sera différent en raison de l'ajout du sel unique.

Cette différenciation des hashs rend inefficace l'utilisation de tables arc-en-ciel, car celles-ci reposent sur la précomputation de couples de mots de passe et de hashs correspondants. En ajoutant du sel, la relation entre un mot de passe et son hash devient spécifique à chaque utilisateur, compromettant ainsi la validité des tables arc-en-ciel précalculées. En résumé, l'utilisation du sel renforce la sécurité en introduisant une variabilité individuelle dans le processus de hachage, dissuadant les attaquants de recourir à des méthodes précalculées pour déchiffrer les mots de passe.

### Bonus

Nous avons ajouté une fonction permettant de choisir la taille minimum et maximum. Ce paramètre est visible dans la commande --custom_help
