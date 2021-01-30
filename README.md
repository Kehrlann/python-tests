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

---

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

---

---

## Exercice 2: Écrire des tests

Le deuxième exercice un "kata" - un exercice connu, créer pour la pratique, dans l'esprit des katas de karaté. Ce kata a été créé par Roy Osherove, avec la [version originale ici](https://osherove.com/tdd-kata-1). L'idée du kata est de pratiquer le TDD, donc de toujours écrire un test avant de d'écrire du code.

Vous devez écrire des tests pour chacune des fonctionnalités de l'exercice dans `string-calculator/test_calculator.py` ; et l'implémentation dans `string-calculator/calculator.py`. Vous pouvez éxécuter les tests avec:

```
$ pytest string-calculator/test_calculator.py
```

### Énoncé (traduit)

Trois règles, qui rendent cet exercice intéressant:

1. Essayez de ne pas lire "à l'avance" les consignes
2. Faites une seule consigne à la fois (sans lire la suivante). Tout l'intérêt de l'exercice est d'apprendre à travailler de manière incémentale.
3. Ne testez que des chaînes de caractères **valides**. Pas la peine de s'encombrer des cas non valides ou non spécifiés.

Vraiment ! Arrêtez vous à chaque séparateur "ligne" comme ci-dessous:

---

---

---

#### 1. Add

Implémentez la fonction `add` dans `string-calculator/calculator.py`. Cette fonction prend en entrée une chaîne de caractères, et renvoie un entier:

```python
def add(input_str: str) -> int:
    # ...
```

La chaîne de caractères contient jusqu'à deux entiers, séparés par des virgules. La fonction renvoie leur somme.

Par exemple, `""`, `"1"` ou `"1,2"`. Pour `""`, ça renvoie 0.

- Commencez par le cas le plus simple, la chaîne vide (c'est déjà fait pour vous).
- Puis passez à chacun des cas suivants.
- Avant chaque cas, écrivez un test!
- Rappelez-vous: il faut résoudre les choses le plus simplement possible, et ne pas faire "plusieurs cas" d'un coup.
- A chaque fois que vos tests sont au vert, réfléchissez à comment améliorer votre code, le rendre plus simple, etc (faites du _refactoring_).

Hop hop hop. On ne lit pas la suite.

---

---

---

#### 2. Nombre illimité d'entiers

Changez `add` pour prendre un nombre inconnu d'entiers.

N'oubliez pas de commencer par le test ...

---

---

---

#### 3. Saut de ligne comme délimiteur

Permettez l'utilisation d'un saut de ligne (c'est à dire `\n`) comme délimiteur, en plus de la virgule.

Par exemple, `1\n2,3` donnera 6. Pour ceux qui se posent des questions, notez que `1,\n` n'est pas une entrée valide (mais pas besoin d'écrire un test, c'est juste une clarification).

---

---

---

#### 4. Délimiteur configurable

Pour choisir un délimiteur différent, la chaîne commencera par une ligne du style `//<DELIMITEUR>\n`, où `<DELIMITEUR>` est un caractère unique, suivi d'une ligne avec les nombres.

Par exemple, `//;\n1;2` renverra 3 - le délimiteur est ici `;`.

La première ligne est optionnelle, tous les scénarios précédents doivent continuer de fonctionner.

---

---

---

#### 5. Entiers négatifs

Appeler `add` avec un entier négatif renverra un message d'erreur, qui commencera par `negatives not allowed` et contiendra l'entier négatif contenu dans la chaîne.

S'il y a plusieurs entiers négatifs, affichez-les tous dans le message d'erreur.

(Vous avez remarqué ? Il y avait deux cas, ici!)

---

---

---

**STOP** L'exercice original recommande aux débutants de s'arrêter ici... Mais l'exercice 3 du TP sera plus compliqué, donc je vous recommande de continuer un peu :)

---

---

---

#### 6. Entiers supérieurs à 1000

Les entiers supérieurs à 1000 doivent être ignorés, donc `2 + 1001 = 2`.

---

---

---

Ici ca va commencer à se corser un peu. Certains d'entre vous seront contents d'avoir écrit des tests, parce que vous risquez de faire bugger certains des cas précédents...

---

---

---

#### 7. Délimiteurs avec plusieurs caractères

Les délimiteurs peuvent avoir autant de caractères que souhaité, avec le format suivant: `//[<DELIMITER>]\n`. Par exemple `//[***]\n1***2***3` renverra 6.

Hint: ici, les expressions régulières peuvent être utiles... Mais pas obligatoires!

---

---

---

#### 8. _Ultimate Grand Finale_

Autorisez autant de délimiteurs que souhaité, selon le format: `//[delim1][delim2][delim3]\n`. Par exemple `//[*][%]\n1*2%3` renverra 6.

Vous devez supporter des délimiteurs de longueur >= 1 caractère.
