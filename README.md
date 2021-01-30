# python-tests

## Installation des dépendances avec Conda

### Conda

Normalement vous avez installé et activé conda durant les cours d'install du premier semestre.

En utilisant votre terminal, placez vous dans le répertoire que vous venez de cloner et puis faites:

```
$ conda create --file requirements.txt --name python-testing
$ conda activate python-testing
$ pytest
```

### Autres

Si vous utilisez un autre gestionnaire d'environnements, ou si vous voulez installez sur votre Python système, vous pouvez utiliser le fichier `requirements.txt`

## Exécuter des tests

Il suffit dans lancer `pytest`, comme dans l'exemple d'installation.

```
$ pytest
```

Vous pouvez également lancer un test en particulier:

```
$ pytest fizzbuzz/test_fizzbuzz.py
```

--- 

## Exercice 1

Pour le premier exercice, une suite de tests est disponible dans `fizzbuzz/test_fizzbuzz.py` . Vous devez implémenter la fonctionnalité dans le fichier `fizzbuzz/fizzbuzz.py` . À vous de lire le fichier de tests pour comprendre ce que doit faire `fizzbuzz` puis de l'implémenter. Une fois l'exercice terminé, tous les tests liés doivent être verts!

Vous pouvez éxécuter les tests de cet exercice avec:

```
$ pytest fizzbuzz/test_fizzbuzz.py
```

Ou bien, un par un:

```
$ pytest fizzbuzz/test_fizzbuzz.py::test_returns_a_list
```