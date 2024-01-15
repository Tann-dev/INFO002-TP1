# TP1 Cryptologie - Compromis temps / mémoire, les tables arc-en-ciel

#### Antoine DEPOISIER & Irilind SALIHI

Des détails sur les commandes sont disponibles en effectuant les commandes :

```shell
python .\main.py --custom_help
python .\main.py --test_help
```

### Question 8

Si aucun décalage ne serait effectuer, il se peut que l'on tomberait dans une boucle, et que l'on recouvre seulement une partie de la table qui a bouclé sur elle même.

### Question 11

Nous avons essayeé avec la suite de commande qui suit pour cracker un hash :
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

### Question 14

On fait déjà le test pour le premier alphabet avec un mot à 4 caractères.
Je regarde déjà la couverture de matable, pour connaître combien de lignes j'ai besoin à peu près.

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

Le temps de calcul des tables est d'environ 5 secondes
Le temps de calcul de l'inverse est presque instantanné


Nous essayons ensuite avec un alphabet plus grand, et un nouvel alphabet

```shell
python .\main.py --abc=40 --size=5 --stats --width=200 --height=1000000
Couverture : 74.57689803230222
```

```shell
python .\main.py --abc=40 --size=5 --load=crack.txt --creer_table_fichier --height=1000000 --width=200
```

```shell
python .\main.py --abc=40 --size=5 --load=crack.txt --crack --width=200 --hash_to_crack=dafaa5e15a30ecd52c2d1dc6d1a3d8a0633e67e2
Les résultat trouvé est : n00b.
```

Le temps de calcul des tables est d'environ 520 secondes, soit 8 minutes 40
Le temps de calcul de l'inverse est d'environ 1.4 secondes.

Quand aucun n'est trouvé, il est d'environ 5 secondes.


### Question 15

Nous avons regardé avec la fonction stats, combien il faudrait de ligne dans notre table arc en ciel pour pouvoir avoir une couverture haute.

```shell
python .\main.py --abc=36 --size=8 --stats --width=200 --height=100000000000
Couverture : 95.33362839981649
```

On voit qu'il nous faut donc 100 000 000 000 pour pouvoir craquer presque tous les mots de passes.

Pour 1 000 000 il nous fallait environ 500 secondes, donc là, on a multiplié par 100 000, donc environ 50 000 000 secondes. Ce quii représente 578.7 jours. Tout ça juste pour générer la table arc en ciel.

Pour cracquer, près de 500 000 secondes, soit 5.787 jours.