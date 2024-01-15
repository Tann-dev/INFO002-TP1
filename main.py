import argparse
from questions import *
from tests import *

def main():
    config = ConfigGlobal()


    parser = argparse.ArgumentParser(description="Exemple de fonction de hachage SHA-1")
    parser.add_argument("--hash", action="store_true", help="Hasher un mot")
    parser.add_argument("--show_config", action="store_true", help="Voir la configuration courante")
    parser.add_argument("--crack", action="store_true", help="Trouver l'inverse d'un hash, il est nécessaire d'avoir le paramètre --wordToCrack=, une table arc en ciel dans un fichier --load= et --width=")
    parser.add_argument("--crack_exhaustive", action="store_true", help="Trouver l'inverse d'un hash, il est nécessaire d'avoir le paramètre --wordToCrack=, une table arc en ciel dans un fichier --load= et --width=")
    parser.add_argument("--i2c", action="store_true", help="Trouver le texte clair correspondant à l'indice donné en paramètre avec la configuration courante")
    parser.add_argument("--h2i", action="store_true", help="h2i d'un hash avec la configuration courante")
    parser.add_argument("--nouvelle_chaine", action="store_true", help="Parcours la chaine pour nous donner l'index résultat de l'index donné en parramètre, il est nécéssaire d'avoir les paramètres --wordIndex= et --width=")
    parser.add_argument("--creer_table_fichier", action="store_true", help="Créer une table dans le fichier selectionné, il est nécéssaire d'avoir les paramètres --load=, --width= et --height=")
    parser.add_argument("--affiche_table", action="store_true", help="Affiche un résumé d'un table d'un fichier, il est nécéssaire d'avoir le paramètre --load=")
    parser.add_argument("--stats", action="store_true", help="Connaître la couverture de notre table, il est nécéssaire d'avoir les paramètres --width= et --height=")

    parser.add_argument("--test", action="store_true", help="Permet d'executer un test pour une fonctionnalité")

    parser.add_argument("--custom_help", action="store_true", help="Connaitre les détails des commandes disponibles")
    parser.add_argument("--test_help", action="store_true", help="Avoir des exemples des tests d'utilisation")

    # Optionnal parameters
    parser.add_argument('--size', type=config.setTaille)
    parser.add_argument('--alphabet', type=config.setAlphabet)
    parser.add_argument('--abc', type=config.setABC)
    parser.add_argument('--load', default=".", type=config.setFile)

    # Optionnal parameters for questions
    parser.add_argument('--word_index', default=1234, type=int)
    parser.add_argument('--word', default="oups", type=str)
    parser.add_argument('--width', default=1, type=int) # Q9 / Q10
    parser.add_argument('--height', default=1, type=int) # Q9 / Q10
    parser.add_argument('--hash_to_crack', default="oups", type=str)

    args = parser.parse_args()

    if args.hash:
        if args.test:
            hashTest()
        else:
            hash(args.word)
    elif args.show_config:
        showConfig(config)
    elif args.i2c:
        if args.test:
            i2cTest()
        else:
            i2c(config, args.word_index)
    elif args.h2i:
        if args.test:
            h2iTest()
        else:
            h2i(config, args.word)
    elif args.nouvelle_chaine:
        if args.test:
            nouvelleChaineTest()
        else:
            nouvelleChaine(config, args.word_index, args.width)
    elif args.creer_table_fichier:
        if args.test:
            creerTableFichierTest()
        else:
            creerTableFichier(config, args.width, args.height)
    elif args.affiche_table:
        if args.test:
            afficheTableTest()
        else:
            afficheTable(config)
    elif args.crack:
        if args.test:
            crackTest()
        else:
            crack(config, args.hash_to_crack, args.width)
    elif args.crack_exhaustive:
        crackExhaustive(config, args.hash_to_crack, args.width)
    elif args.stats:
        stats(config, args.width, args.height)
    elif args.custom_help:
        getHelp()
    elif args.test_help:
        getTestExamples()
    else:
        print("Aucun argument spécifié. Utilisez --custom_help pour connaitre les commandes disponibles")

if __name__ == "__main__":
    main()
