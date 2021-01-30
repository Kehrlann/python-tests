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

## Exercice 1: Lire des tests

Pour le premier exercice, une suite de tests est disponible dans `fizzbuzz/test_fizzbuzz.py` . Vous devez implémenter la fonctionnalité dans le fichier `fizzbuzz/fizzbuzz.py` . À vous de lire le fichier de tests pour comprendre ce que doit faire `fizzbuzz` puis de l'implémenter. Une fois l'exercice terminé, tous les tests liés doivent être verts!

Vous pouvez éxécuter les tests de cet exercice avec:

```
$ pytest fizzbuzz/test_fizzbuzz.py
```

Ou bien, un par un:

```
$ pytest fizzbuzz/test_fizzbuzz.py::test_returns_a_list
```

---

## Exercice 2: Écrire des tests

Le deuxième exercice un "kata" - un exercice connu, créer pour la pratique, dans l'esprit des katas de karaté. Ce kata a été créé par Roy Osherove, avec la [version originale ici](https://osherove.com/tdd-kata-1).

Vous devez écrire des tests pour chacune des fonctionnalités de l'exercice dans `string-calculator/test_calculator.py` ; et l'implémentation dans `string-calculator/calculator.py`. Vous pouvez éxécuter les tests avec:

```
$ pytest string-calculator/test_calculator.py
```

### Énoncé

```
    Create a simple String calculator with a method signature:

    ———————————————

    int Add(string numbers)

    ———————————————

    The method can take up to two numbers, separated by commas, and will return their sum. 

    for example “” or “1” or “1,2” as inputs.

    (for an empty string it will return 0) 

    Hints:

    ——————

     - Start with the simplest test case of an empty string and move to one and two numbers

     - Remember to solve things as simply as possible so that you force yourself to write tests you did not think about

     - Remember to refactor after each passing test

    ———————————————————————————————

    Allow the Add method to handle an unknown amount of numbers

    ————————————————————————————————

    Allow the Add method to handle new lines between numbers (instead of commas).

        the following input is ok: “1\n2,3” (will equal 6)

        the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)

        ——————————————————————————————-

    Support different delimiters

        to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .

        the first line is optional. all existing scenarios should still be supported

        ————————————————————————————————

    Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. 

    if there are multiple negatives, show all of them in the exception message.

    ————————————————————————————————

    STOP HERE if you are a beginner. Continue if you can finish the steps so far in less than 30 minutes.

    ————————————————————————————————

    Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2

    ————————————————————————————————

    Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6

    ————————————————————————————————

    Allow multiple delimiters like this: “//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.

    ————————————————————————————————

    make sure you can also handle multiple delimiters with length longer than one char

———————————————————————————————— 
```